from django.contrib import admin
from django.urls import path
from .views import list_Court,Update_court,delete_court
from . import views

urlpatterns = [
    path('list/',list_Court),
    path('update/<int:pk>/',Update_court),
    path('delete/<int:pk>/',delete_court),
    path('search/',views.Search_Court)
    
]
