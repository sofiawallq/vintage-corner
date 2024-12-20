from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from shopping_cart.contexts import cart_contents
import stripe
import json


stripe.api_key = settings.STRIPE_SECRET_KEY


@require_POST
def cache_checkout_data(request):
    """
    Caches checkout data into the session to save information
    for Stripe PaymentIntent.
    This view receives the POST data from the checkout form,
    checks if the user wants to save their profile information,
    and modifies the Stripe PaymentIntent with relevant cart and user data.
    The data is then stored in the session for use
    during the payment confirmation process.
    Returns a response with status 200 if data was successfully cached,
    or status 400 if an error occurs during processing.
    """
    try:
        request.session['save_info'] = 'save-info' in request.POST

        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handles the checkout process by displaying the order form,
    creating a Stripe PaymentIntent, and processing the form data for payment.
    This view retrieves the cart from the session, calculates the total amount,
    and allows the user to fill out the order form. If the order form
    is valid, the order is saved and line items are associated with the order.
    If the user opts in to save their profile information,
    it is updated in the profile model.
    Returns a response with the checkout form or a redirect after
    a successful checkout.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

            if 'save-info' in request.POST:
                if request.user.is_authenticated:
                    profile = UserProfile.objects.get(user=request.user)
                    profile_data = {
                        'default_full_name': order.full_name,
                        'default_email': order.email,
                        'default_phone_number': order.phone_number,
                        'default_street_address1': order.street_address1,
                        'default_street_address2': order.street_address2,
                        'default_postcode': order.postcode,
                        'default_town_or_city': order.town_or_city,
                        'default_county': order.county,
                        'default_country': order.country,
                    }
                    user_profile_form = UserProfileForm(profile_data,
                                                        instance=profile)
                    if user_profile_form.is_valid():
                        user_profile_form.save()
                    else:
                        messages.error(request,
                                       'There was an error saving your profile.'
                                       )
                else:
                    messages.error(request,
                                   'You must be logged in to save your profile.'
                                   )

            for item_id in cart.keys():
                try:
                    product = Product.objects.get(id=int(item_id))
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request,
                                   "One of the products in your bag wasn't "
                                   "found in our database. "
                                   "Please contact us for assistance."
                                   )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request,
                           "There are no items in your shopping cart "
                           "at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any
        # info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name() or profile.default_full_name,
                    'email': profile.user.email or profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles a successful checkout by associating the order with
    the user's profile, marking products as unavailable,
    and sending a confirmation message.
    This view is triggered after a successful payment.
    It ensures the user's profile is updated with the new order information,
    marks purchased products as unavailable, and clears the cart session.
    Returns a response displaying the order details and success message.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        save_info = request.session.get('save_info', False)

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
            else:
                messages.error(request,
                               'We could not save your information to your '
                               'profile, please try again.')

    order_line_items = order.lineitems.all()
    for item in order_line_items:
        product = item.product
        product.is_available = False
        product.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)