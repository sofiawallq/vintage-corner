from django.contrib import admin
from .models import Review, Response

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'comment', 'created_at')
    ordering = ('-created_at',)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'comment', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Review, ReviewAdmin)
admin.site.register(Response, ResponseAdmin)
