from django import forms
from .models import ContactStore


class ContactStore(forms.ModelForm):
    """
    Form for creating and sending messages/inquiries to the store.
    This form is connected to the admin panel for administration.
    """
    class Meta:
        model = ContactStore
        fields = ('subject', 'name', 'email', 'message')
