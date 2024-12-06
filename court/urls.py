from django.contrib import admin
from django.urls import path
from .views import list_Court,Update_court,delete_court

urlpatterns = [
    path('list/',list_Court),
    path('update/',Update_court),
    path('delete/<int:pk>/',delete_court)
    
]
