from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product, Category
from products.views import all_products

# Create your views here.
def index(request):
    """ A view to return the home/index page with products """
    products = Product.objects.all().order_by('-created_on')[:3]

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
