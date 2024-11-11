from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review, Response
from profiles.models import UserProfile
from .forms import ReviewForm, ResponseForm


def review_list(request):
    reviews = Review.objects.all()
    current_sort = request.GET.get('sort', '')

    if current_sort == 'date':
        reviews = reviews.order_by('-created_at')
    elif current_sort == 'product':
        reviews = reviews.order_by('product__name')

    if request.method == 'POST' and 'review_form' in request.POST:
        if request.user.is_authenticated:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.user = request.user
                new_review.save()
                return redirect('review_list')
        else:
            review_form = ReviewForm(request.POST)
            return render(request, 'reviews/review_list.html', {
                'reviews': reviews,
                'review_form': review_form,
                'current_sort': current_sort,
                'login_prompt': 'You must be logged in to submit a review.',
            })

    else:
        review_form = ReviewForm()

    if request.method == 'POST' and 'response_form' in request.POST:
        if request.user.is_authenticated:
            response_form = ResponseForm(request.POST)
            review_id = request.POST.get('review_id')
            review = get_object_or_404(Review, id=review_id)

            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.review = review
                response.user = request.user
                response.save()
                return redirect('review_list')
        else:
            response_form = ResponseForm(request.POST)
            return render(request, 'reviews/review_list.html', {
                'reviews': reviews,
                'response_form': response_form,
                'current_sort': current_sort,
                'login_prompt': 'You must be logged in to submit a response.',
            })

    else:
        response_form = ResponseForm()

    return render(request, 'reviews/review_list.html', {
        'reviews': reviews,
        'review_form': review_form,
        'response_form': response_form,
        'current_sort': current_sort,
        'login_prompt': None,
    })