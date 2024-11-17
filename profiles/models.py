from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default delivery information
    and user order history.
    This model extends the built-in Django User model by
    adding fields for default contact and delivery details,
    making it easier for users to manage recurring order information.
    Methods:
        __str__(): Returns the username associated
        with the profile as its string representation.
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=254, null=True,
                                         blank=False)
    default_email = models.EmailField(max_length=254, null=False, blank=False)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create or update the UserProfile instance when
    a User instance is created or saved.
    This function listens for the `post_save` signal on the User model. 
    If a new User instance is created, it also creates a corresponding 
    UserProfile instance. For existing users, it ensures the associated 
    UserProfile is updated when the User instance is saved.
    """
    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
