from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# import for form register
from .forms import RegisterForm
from django.views.generic.base import TemplateView
from django.http import HttpRequest
from django.contrib.auth import logout

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

class SignedOutView(TemplateView):

    template_name = "registration/signed_out.html"

    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)