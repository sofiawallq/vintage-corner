from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    A form for updating the users profile information.
    This form allows users to edit their default contact
    and delivery information.
    It customizes the form's widgets to include placeholders, adds CSS classes,
    and removes auto-generated labels for a cleaner user interface.
    The first field is set to autofocus for good UX.
    Meta:
        model (UserProfile): Specifies the `UserProfile` model for the form.
        exclude: Specifies fields that should be excluded from the form,
        in this case, the 'user' field.
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
