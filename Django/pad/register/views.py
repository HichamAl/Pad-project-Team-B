from django.shortcuts import render, redirect
# import for form register
from .forms import RegisterForm

# Create your views here.

# register view 
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = RegisterForm

    return render(response, "register/register.html", {"form":form})

