from django.urls import path
from . import views
from .views import view_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
     path('remove_from_cart/<item_id>/', remove_from_cart, name='remove_from_cart'),
]
