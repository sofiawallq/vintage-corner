from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom file input widget for handling image uploads in Django forms.
    Widget extends Django's built-in `ClearableFileInput` to provide
    custom labels and template customization for file input fields.
    This widget can be used to override the default appearance and behavior of
    file inputs.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
