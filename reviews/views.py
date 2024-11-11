from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review, Response
from profiles.models import UserProfile
from .forms import ReviewForm, ResponseForm


@login_required
def add_review(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})


@login_required
def add_response(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.review = review
            response.user = request.user
            response.save()
            return redirect('review_detail', review_id=review.id)
    else:
        form = ResponseForm()
    return render(request, 'add_response.html', {'form': form, 'review': review})
