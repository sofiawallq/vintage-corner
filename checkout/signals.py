from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Signal receiver to update the order total when an OrderLineItem is saved.
    This function is triggered when a new OrderLineItem is created,
    or an existing one is updated. It ensures that the total price of the
    associated order is recalculated whenever a line item is added or modified.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Signal receiver to update the order total when an OrderLineItem is deleted.
    This function is triggered when an OrderLineItem is deleted. It ensures that the
    total price of the associated order is recalculated when a line item is removed.
    """
    instance.order.update_total()
