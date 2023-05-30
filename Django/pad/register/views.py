from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.base import TemplateView
from django.http import HttpRequest
from django.contrib.auth import logout
from django.contrib import messages

# register view 
def register(response):
    # if a user registers for an account the form gets submitted
    if response.method == "POST":
        form = RegisterForm(response.POST)
        # if the form is valid it gets saved and the account is created
        if form.is_valid():
            form.save()
            messages.success(response, 'Your account has been successfully created!')
            return redirect("/login")
    else:
        form = RegisterForm

    return render(response, "register/register.html", {"form":form})

# sign out view
class SignedOutView(TemplateView):
    # set the template to the right html file
    template_name = "registration/signed_out.html"
    def get(self, request: HttpRequest):
        # if a user goes to /logout this gets activated and the user gets logged out
        logout(request)
        return render(request, self.template_name)