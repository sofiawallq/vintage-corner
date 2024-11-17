from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Constructs and returns the context for the shopping cart in a dictionary.
    Retrieves the contents of the shopping cart from the session data
    and calculates total cost, number of products, delivery fee,
    and the grand total. If the total cost is below the free delivery
    threshold defined in the settings, a delivery charge is applied
    as a percentage of the total.
    """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id in cart.keys():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        product_count += 1

        cart_items.append({
            'item_id': item_id,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
