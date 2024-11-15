from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'comment', 'created_at', 'is_approved')
    ordering = ('-created_at',)

admin.site.register(Review, ReviewAdmin)