from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review, Response
from profiles.models import UserProfile
from .forms import ReviewForm, ResponseForm


def review_list(request):
    """ A view to show all reviews, with optional sort functionality """
    reviews = Review.objects.all()
    sort = request.GET.get('sort', None)
    
    # If the form is submitted to add a review
    if request.method == 'POST' and 'review_form' in request.POST:
        review_form = ReviewForm(request.POST, user_profile=request.user.profile)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        review_form = ReviewForm()

    # If the form is submitted to add a response to a review
    if request.method == 'POST' and 'response_form' in request.POST:
        response_form = ResponseForm(request.POST)
        if response_form.is_valid():
            review_id = request.POST.get('review_id')
            review = get_object_or_404(Review, id=review_id)
            response = response_form.save(commit=False)
            response.review = review
            response.user = request.user
            response.save()
            return redirect('review_list')
    else:
        response_form = ResponseForm()

    # Sorting the reviews if needed
    if sort == 'date':
        reviews = reviews.order_by('-created_at')
    elif sort == 'product':
        reviews = reviews.order_by('product__name')

    context = {
        'reviews': reviews,
        'review_form': review_form,
        'response_form': response_form,
        'current_sort': sort,
    }

    return render(request, 'reviews/review_list.html', context)
