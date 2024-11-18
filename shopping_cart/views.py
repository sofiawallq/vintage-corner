from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ 
    A view that renders the shopping cart contents page.
    """

    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """ 
    Adds a specified product to the shopping cart.
    If the item hasn't been added to the cart already,
    the cart content is increased by one upon user interaction.
    Shows success message accordingly.
    """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in cart:
        messages.error(request, f'{product.name} is already in your shopping cart')
    else:
        cart[item_id] = 1
        messages.success(request, f'Added {product.name} to your shopping cart', extra_tags='cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ 
    Remove a specified product from the shopping cart.
    Upon user interaction the item is removed from the cart
    and the database is updated.
    Shows success message accordingly.
    """

    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})

    if item_id in cart:
        del cart[item_id]
        messages.success(request,
                         f'Removed {product.name} from your shopping cart')

    request.session['cart'] = cart
    return redirect('view_cart')
