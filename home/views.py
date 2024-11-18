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
    products = Product.objects.filter(is_available=True).order_by('-created_on')[:3]

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


def privacy_policy(request):
    """
    A view to render the 'home/privacy_policy.html' template, which contains
    the companys privacy policy.
    """
    return render(request, 'home/privacy_policy.html')

def shipping(request):
    """
    A view to render the 'home/terms_conditions.html' template, which contains
    the companys shipping information.
    """
    return render(request, 'home/shipping.html')


def terms_conditions(request):
    """
    A view to render the 'home/terms_conditions.html' template, which contains
    the companys terms and conditions.
    """
    return render(request, 'home/terms_conditions.html')

