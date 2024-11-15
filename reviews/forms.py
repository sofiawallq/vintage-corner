from django import forms
from .models import Review
from products.models import Product


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('product', 'comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write your review here', 'rows': 6}),
        }

    def __init__(self, *args, **kwargs):
        user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)
        if user_profile:
            purchased_products = Product.objects.filter(
                orderlineitem__order__user_profile=user_profile
            ).distinct()
            self.fields['product'].queryset = purchased_products
            self.fields['product'].required = False
            self.fields['product'].empty_label = "No product (general review)"
