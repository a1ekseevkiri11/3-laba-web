from django.urls import path
from . import views

urlpatterns = [
    path('calculator/', views.calculator, name='calculator'),
    path('', views.index),
]
