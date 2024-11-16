from django import forms
from .models import ContactStore


class ContactStore(forms.ModelForm):
    """
    Form for creating and sending messages/inquiries to the store.
    This form is connected to the admin panel for administration.
    Contains fields for:
        subject (str) - subject of the question/inquiries.
        name (str) - name of the person filling out the form.
        email (EmailField) - email address of the person filling out the form.
        message (str) - content of the message/question/inquiriy.
    """
    class Meta:
        model = ContactStore
        fields = ('subject', 'name', 'email', 'message')
