from django import forms
from .models import Review
from products.models import Product


class ReviewForm(forms.ModelForm):
    """
    Form for creating reviews submitted by users.
    This form is based on the `Review` model
    and allows users to submit a review with a potential product and comment.
    It includes a custom initialization method that restricts
    the product choices to those the user has purchased. If the user has
    not purchased any products, the product field will be set as optional,
    allowing for a general review.
    Methods:
        __init__(self, *args, **kwargs):
        Custom initialization to filter the `product` field's queryset to
        include only products the user has purchased and set the product
        field as optional if no purchased products are found.
    """
    class Meta:
        model = Review
        fields = ('product', 'comment',)
        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'Write your review here', 'rows': 6
            }),
        }

    def __init__(self, *args, **kwargs):
        user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)

        if user_profile:
            purchased_products = Product.objects.filter(
                order_items__order__user_profile=user_profile
            ).distinct()
            self.fields['product'].queryset = purchased_products
            self.fields['product'].required = False
            self.fields['product'].empty_label = "No product (general review)"
