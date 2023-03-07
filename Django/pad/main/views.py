from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# work in progress
# def profile(response):
    # return render(response, 'main/profile.html')

@login_required(login_url='/login/')
def home(response):
    return render(response, "main/home.html")

def index(response):
    return render(response, "main/index.html")

def enter(response):
    return render(response, "main/enter.html")

@login_required(login_url='/login/')
def challenges(response):
    return render(response, "main/challenges.html")
    
@login_required(login_url='/login/')
def challenges1(response):
    return render(response, "main/challenges-1.html")
