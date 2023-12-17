from django.shortcuts import render,redirect,HttpResponse
from .models import *
import requests
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
import uuid
from .utils import *
from rest_framework import viewsets
from .serializers import *

@login_required
def home(request):
    product = Product.objects.all()
    return render(request,'index.html',{'product':product})

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializers

@login_required
def weather(request):

    if request.method == "POST":
        city = request.POST.get('city')
    
    else:
        city = "Faridabad"

    apik = "3045dd712ffe6e702e3245525ac7fa38"
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apik}'

    data = requests.get(url)
    json_data = data.json()

    temperature = json_data['main']['temp'] - 273.15
    description = json_data['weather'][0]['description']
    icon = json_data['weather'][0]['icon']

    context = {
        'city':city,
        'temperature': temperature,
        'description': description,
        'icon': f'http://openweathermap.org/img/w/{icon}.png',
    }

    return render(request, 'weather.html', context)

@login_required
def visulization(request):
    Data = data.objects.all().values('topic', 'intensity' , 'likelihood' , 'title' , 'relevance' , 'country' , 'end_year')

    topic = [item['topic'] for item in Data]
    title = [item['title'] for item in Data]
    intensity = [item['intensity'] for item in Data]
    likelihood = [item['likelihood'] for item in Data]
    relevance = [item['relevance'] for item in Data]
    country = [item['country'] for item in Data]
    end_year = [item['end_year'] for item in Data]


    context = {
        'topic': topic,
        'intensity': intensity,
        'title': title,
        'likelihood': likelihood,
        'country': country,
        'relevance':relevance,
        'end_year':end_year,
    }
    return render(request,'visulization.html',context)

class DataViewset(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class = dataSerializers

def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request, username = username , password = password)
        if user is not None:
            auth_login(request,user)
            return redirect('/')
        else :
            message = "Invalid username or password. Please try again."

    return render(request, 'login.html', {'messege':message})

def logout(request):
    auth_logout(request)
    return redirect("/login/")

def sign_up(request):
    messege = ''
    if request.method == "POST":
        username = request.POST['username']
        first_name=request.POST["first-name"]
        last_name=request.POST["last-name"]
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re-password']

        if password == re_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username,password=re_password,first_name=first_name,last_name=last_name,email=email)
                email_token = str(uuid.uuid4())
                print(email_token,"Deepak")
                profile = Profile.objects.create(user = user , email_token = email_token)
                send_email_token(email , profile.email_token)
                messege = "Account Create Successful"
            else:
                messege = "Username already exists."
        else:
            messege = "Passwords do not match."

        print(messege)
    return render(request, 'signup.html' ,{'messege':messege})

def verify(request,token):
    print(f"Received token: {token}")
    try:
        profile = Profile.objects.get(email_token= token )
        profile.is_verify = True
        profile.save()
        return HttpResponse("Your account Verified")
    except Exception as e:
        return HttpResponse("Invalid Token")