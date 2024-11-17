import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    A model to represent a customer order, containing order details such as
    shipping information, total amounts, and payment details.
    Methods:
        _generate_order_number: Generates a unique order number using UUID.
        update_total: Updates the order's total,
        including recalculating delivery costs.
        save: Overrides the save method to generate an order number
        if it is not set.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        Returns the generated order number in uppercase.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total of the order each time a line item is added,
        accounting for delivery costs.
        The updated values are saved to the order instance.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))
        ['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to generate and set the order number
        if it hasn't been set already.
        This ensures that each order gets a unique order number before
        it is saved to the database.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    A model to represent an individual product line item within an order.
    Methods:
        save: Overrides the save method to calculate the lineitem_total
        and ensure the order total is updated.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=True, blank=False,
                                on_delete=models.SET_NULL,
                                related_name='order_items')
    product_name = models.CharField(max_length=250, null=True, blank=True)
    product_price = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=True, blank=True)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to calculate
        and set the lineitem total.
        The lineitem_total is calculated as the product price.
        This method also updates the total price of the associated order.
        Returns a string describing the line item with product SKU
        and associated order number.
        """
        self.product_name = self.product.name if self.product else self.product_name
        self.product_price = self.product.price if self.product else self.product_price
        self.lineitem_total = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
