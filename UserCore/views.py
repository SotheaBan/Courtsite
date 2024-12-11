from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .form import RegisterForm,loginForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# Create your views here.


@api_view(['POST'])
def RegisterUser(request): 
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home_view(request) :

    return render(request,'home.html')  

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user) 
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
     

    return render(request, 'register.html', {'form': form})  





def login_view(request):
    if request.method == 'POST':
        form = loginForm(request, data=request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  
                return redirect('home') 
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})


