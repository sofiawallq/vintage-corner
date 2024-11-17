import random
import string
from django.db import models


def generate_sku():
    """
    Generates a random and unique SKU composed
    of uppercase letters and digits with a length of 8 characters,
    for each new product that is added to the store.
    It is called by the Product model to automatically generate a SKU
    when a new product is added to the store.
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


class Category(models.Model):
    """
    This model is used to categorize products in the store.
    Each category has a name and an optional friendly name
    that can be used for display purposes.
    Methods:
        __str__(): Returns the name of the category.
        get_friendly_name(): Returns the friendly name of the category
        if it exists, otherwise returns the category name.
    Meta:
        verbose_name_plural (str): Specifies the plural form of the category name
        in the Django admin (i.e., 'Categories').
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    This model stores all the relevant information about a product,
    including its name, category, description, price, image, SKU,
    and availability status.
    Methods:
        __str__(): Returns the name of the product.
    Meta:
        verbose_name_plural (str): Specifies the plural form of the product name
    """
    
    name = models.CharField(max_length=250)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to='product_images/')
    sku = models.CharField(max_length=250, unique=True, default=generate_sku)
    created_on = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

