from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def view_cart(request):
    """ A view that renders the shopping cart contents page """

    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """ Add the specified product to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id not in cart:
        cart[item_id] = 1

    request.session['cart'] = cart
    return redirect(redirect_url)
