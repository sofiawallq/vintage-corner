from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.contrib import messages


def user_logged_in_handler(request, user, **kwargs):
    """
    This signal handles user login and checks if the user has verified
    their email address. If the user has not verified their email,
    a message is displayed asking for email verification.
    """
    if not user.email_verified:
        messages.warning(request, "Please verify your email address "
                         "to complete your registration.")
    else:
        messages.success(request, "Welcome back!")
