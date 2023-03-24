from django.contrib import admin
from .models import UserPoints, Challenge

# Register your models here.

admin.site.register(Challenge)
admin.site.register(UserPoints)
