from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib.auth import logout


@login_required
def profile(request):
    """
    Display and update the users profile.
    This view retrieves the profile of the currently authenticated user,
    and displays it in a form. If request method is POST,
    it attempts to update the profile with the submitted data and
    shows a success or error message accordingly.
    Additionally, the view fetches all orders associated
    with the users profile.
    Returns a rendered HTML page with users profile form and a list of orders.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def delete_account(request):
    """
    Handles the deletion of the currently logged-in users account and profile.
    This view processes the account deletion request. 
    It logs out the user before deletion to prevent any issues.
    Deletes the associated user profile if it exists.
    Deletes the user's account from the system.
    If a user attempts to delete their account via a
    GET request or invalid method, a 404 error will be raised,
    as only POST requests are allowed for this action.
    Returns a redirect to the home page with a success message
    if account deletion is successful.
    Or redirects to the profile page with an error message if
    there is a problem deleting the account.
    """
    if request.method == 'POST':
        try:
            user = request.user
            logout(request)
            sleep(2)

            profile = user.userprofile
            profile.delete()

            user.delete()
            
            messages.success(request, "Your account has been successfully deleted.")
            return redirect('home')

        except UserProfile.DoesNotExist:
            messages.error(request, "An error occurred while trying to delete your account.")
            return redirect('profile')

    else:
        raise Http404("Page not found. Only POST method is allowed.")


def order_history(request, order_number):
    """
    Display a past order confirmation for the user.
    This view retrieves an order by its order number
    and displays it as a past order confirmation.
    It also notifies the user that the displayed page is a
    historical confirmation, and that an email confirmation
    was sent on the original order date.
    Returns a rendered HTML page showing order details and context
    indicating it is viewed from the users profile.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
