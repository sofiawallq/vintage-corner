from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('add_response/', views.add_response, name='add_response'),
    path('add_review/', views.add_review, name='add_review'),
]