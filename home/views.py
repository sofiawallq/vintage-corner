from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product, Category
from products.views import all_products


def index(request):
    """
    A view to return the home/index page with the most recently products.
    This view queries the database for the three most recently created products
    and passes them to the context for rendering the index page.
    Renders the 'home/index.html' template with the products context.
    """
    products = Product.objects.all().order_by('-created_on')[:3]

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """
    A view to render the 'home/about.html' template, which contains
    information about the company.
    """
    return render(request, 'home/about.html')

