from django.urls import path
from . import views

urlpatterns = [
    path('roads/', views.road_list, name='road_list'),
]