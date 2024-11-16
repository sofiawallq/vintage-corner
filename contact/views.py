from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactStore


def contact_store(request):
    """
    Handles the contact form for customers to send messages to the store.
    Manages the display and submission of the contact form, allowing
    customers to send inquiries. If the request method is POST and
    form is valid, the message is saved to database and a success message
    is displayed. Otherwise, the form is re-rendered.
    Returns either the contact form or a confirmation
    if the form submission is successful.
    """
    contact_form = ContactStore()

    if request.method == "POST":
        contact_form = ContactStore(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('/contact/?success=true')

    return render(
        request,
        'contact/contact.html',
        {
            'contact_form': contact_form
        },
    )
