from django.contrib import admin
from .models import ContactStore
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(ContactStore)
class ContactStoreAdmin(admin.ModelAdmin):

    list_display = ('subject', 'name', 'message', 'read',)