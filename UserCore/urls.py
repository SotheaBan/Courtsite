from django.urls import path
from dj_rest_auth.views import LoginView
from .views import register,login_view,home_view,RegisterUser


booking = 'booking'

urlpatterns = [

    #path('login/',LoginView.as_view()),
    #path('register/', RegisterUser),
    
    path('login/',login_view),
    path('register/', register),
    path('home/',home_view, name='home'),

]