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
    sort_by = request.GET.get('sort', '')
    reviews = Review.objects.filter(is_approved=True)

    if sort_by == 'date':
        reviews = reviews.order_by('-created_at')
    elif sort_by == 'product':
        reviews = reviews.order_by('product__name')
        
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
                    messages.error(request, 'You can only review products that you have purchased.')
                    return redirect('add_review')
            
            review.is_approved = False
            
            review.save()
            messages.success(request, 'Your review has been submitted and is awaiting approval.')
            return redirect('review_list')
    else:
        form = ReviewForm(user_profile=user_profile)
    
    return render(request, 'reviews/add_review.html', {
        'form': form,
    })
