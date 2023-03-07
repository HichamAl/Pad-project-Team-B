from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(response):
#    return render(response, "main/index.html")
def profile(response):
    return render(response, 'main/profile.html')

def home(response):
    return render(response, "main/home.html")

def index(response):
    return render(response, "main/index.html")

def enter(response):
    return render(response, "main/enter.html")

def challenges(response):
    return render(response, "main/challenges.html")

def challenges1(response):
    return render(response, "main/challenges-1.html")
