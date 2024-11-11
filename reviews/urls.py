from django.urls import path
from . import views

urlpatterns = [
    path('add_review/', views.add_review, name='add_review'),
    path('review/<int:review_id>/add_response/', views.add_response, name='add_response'),
    path('reviews/', views.review_list, name='review_list'),
]