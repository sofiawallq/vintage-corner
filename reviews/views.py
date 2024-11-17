from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Review
from checkout.models import OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from .forms import ReviewForm


def review_list(request):
    """
    This function retrieves all approved reviews from
    the database and applies sorting based on query parameter.
    The reviews can be sorted by date or by the name of a product.
    The function also handles pagination to display a
    limited number of reviews per page.
    Returns a rendered HTML page displaying a list of reviews,
    current sorting and pagination details.
    """
    sort_by = request.GET.get('sort', '')
    reviews = Review.objects.filter(is_approved=True)

    if sort_by == 'date':
        reviews = reviews.order_by('-created_at')
    elif sort_by == 'product':
        reviews = reviews.order_by('product__name')
    else:
        reviews = reviews.order_by('-created_at')

    paginator = Paginator(reviews, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'reviews/review_list.html', {
        'reviews': page_obj.object_list,
        'current_sort': sort_by,
        'page_obj': page_obj,
    })


@login_required
def add_review(request):
    """
    Allows authenticated users to submit either a general review
    or for a product they have purchased.
    This function handles both the display and submission of the review form.
    If the form is submitted, the function checks if the user has purchased
    the product they wish to review.
    If not an error message is shown accordingly.
    Valid submissions are saved but marked as not approved, pending moderation.
    Returns a rendered HTML page showing the review form and redirects to the
    review list with appropriate messages.
    """
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user

            if review.product:
                has_purchased = OrderLineItem.objects.filter(
                    order__user_profile=user_profile,
                    product=review.product
                ).exists()

                if not has_purchased:
                    messages.error(request, 'You can only review products '
                                   'that you have purchased.')
                    return redirect('add_review')

            review.is_approved = False

            review.save()
            messages.success(request,
                             'Your review has been submitted '
                             'and is awaiting approval.')
            return redirect('review_list')
    else:
        form = ReviewForm(user_profile=user_profile)

    return render(request, 'reviews/add_review.html', {
        'form': form,
    })
