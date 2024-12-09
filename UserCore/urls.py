from django.urls import path
from dj_rest_auth.views import LoginView
from .views import RegisterUser




urlpatterns = [

    path('login/',LoginView.as_view()),
    path('register/', RegisterUser)
]