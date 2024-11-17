from django.db import models


class ContactStore(models.Model):
    """
    A model to store customer inquiries or
    contact messages submitted to the store.
    It contains details about the subject, sender's name, email,
    and the message itself, as well as a flag indicating whether the message
    has been read by the store's staff.
    Methods:
        __str__(): Returns a string representation of the message,
        indicating the name of the sender and that it is a customer inquiry.
    """

    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Question from {self.name}"
