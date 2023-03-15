from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# work in progress
def profile(response):
    return render(response, 'main/profile.html')

# home page view
@login_required(login_url='/login/')
def home(response):
    return render(response, "main/home.html")
 
# index page/challenge view
def index(request):
    # if user has not seen index is redirected to index.html 
    # else redirected to the enterpage 
    if 'has_seen_index' not in request.session:
        request.session['has_seen_index']= True
        return render (request, 'main/index.html')
    else:
        return redirect("/enter/")

# enter view
def enter(response):
    return render(response, "main/enter.html")

# challenge page view
@login_required(login_url='/login/')
def challenges(response):
    return render(response, "main/challenges.html")

# challenge 1 view
@login_required(login_url='/login/')
def challenges1(response):
    return render(response, "main/challenges-1.html")
