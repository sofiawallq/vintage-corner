from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review, Response
from profiles.models import UserProfile
from .forms import ReviewForm, ResponseForm


def review_list(request):
    sort_by = request.GET.get('sort', '')
    reviews = Review.objects.all()

    if sort_by == 'date':
        reviews = reviews.order_by('-created_at')
    elif sort_by == 'product':
        reviews = reviews.order_by('product__name')

    return render(request, 'reviews/review_list.html', {
        'reviews': reviews,
        'current_sort': sort_by,
    })


@login_required
def add_response(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            review_id = form.cleaned_data['review_id']
            review = Review.objects.get(id=review_id)
            response = form.save(commit=False)
            response.user = request.user
            response.review = review
            response.save()
            return redirect('review_list')
    return redirect('review_list')


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/add_review.html', {
        'form': form,
    })