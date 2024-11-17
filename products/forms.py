from django import forms
from .models import Product, Category
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    A form for creating and editing products in the store.
    This form is used for handling product data, including the product's
    category, description, price, image, and SKU.
    The form is linked to the `Product` model and allows for
    the creation and editing of products in the admin or store interface.
    Methods:
        __init__(): Initializes the form, setting category choices to use
        friendly names.
    Meta:
        model (Model): The model this form is based on (`Product`).
        fields (tuple): All fields from the `Product` model will be included
        in the form.
    """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
