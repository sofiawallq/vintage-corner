from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to display all products with optional filtering,
    searching, and sorting.
    This view retrieves and displays all available products, applying filters
    based on search queries, category selection,
    and sorting criteria if provided through GET parameters.
    Returns a rendered HTML page displaying the filtered and sorted
    list of products.
    """
    products = Product.objects.filter(is_available=True)
    query = None
    categories = None
    sort = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter a valid search query")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'price':
                products = products.order_by('price')
            elif sort == 'name':
                products = products.order_by('name')
            elif sort == 'news':
                products = products.order_by('created_on')

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sort': sort,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to display detailed information for a specific product.
    This view fetches a product using its unique identifier
    and renders a template displaying detailed information about the product.
    Returns a rendered HTML page showing the product's details.
    product_id (int): The unique identifier of the product to display.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Admin - Allow store admins/superusers to add a new product to the store.
    This view displays a form for adding a new product.
    If the form is submitted and valid,
    the new product is saved to the database.
    Error messages are shown if the form is invalid
    or if the user is unauthorized.
    Returns a rendered HTML page with the product form or a redirect
    upon successful submission.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. '
                           'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Admin - Allow store admins/superusers to edit an existing product.
    This view fetches a specific product for editing and displays a form
    pre-filled with the product's current data.
    Form submissions update the product if valid, while unauthorized
    users are redirected with an error.
    Returns a rendered HTML page with the product form or a redirect
    upon successful submission.
    product_id (int): The unique identifier of the product to edit.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. '
                           'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Admin - Allow store admins/superusers to delete a product from the store.
    Unauthorized access attempts are redirected with an error message.
    Returns a redirect to the main products page after deletion.
    product_id (int): The unique identifier of the product to delete.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
