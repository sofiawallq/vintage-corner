from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Model that represents a product review submitted by a user.
    Stores reviews that users submit for products/general site.
    Each review contains the potential product it refers to,
    the user who submitted it, the comment text,
    timestamps for creation and an approval status.
    Reviews are associated with products and users via foreign keys.
    A review can only be created once per user-product pair.
    Meta:
        unique_together (tuple): Ensures that each user can
        only submit one review per product.
    Methods:
        __str__(): Returns a string representation of the review,
        showing the product name and the username of the reviewer,
        or indicating 'No Product' if the product is not specified.
    """
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f'Review for {
            self.product.name if self.product else 'No Product'} by {
                self.user.username}'
