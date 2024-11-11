from django import forms
from .models import Review, Response
from products.models import Product


class ReviewForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.none(),
        required=False,
        label="Write a review about a previously bought item (optional)"
    )
    
    class Meta:
        model = Review
        fields = ('product', 'comment')
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write your review here', 'rows': 8}),
        }

    def __init__(self, *args, **kwargs):
        user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)
        if user_profile:
            purchased_products = Product.objects.filter(
                orderlineitem__order__user_profile=user_profile
            ).distinct()
            self.fields['product'].queryset = purchased_products
  

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('comment')
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write your response here', 'rows': 4}),
        }