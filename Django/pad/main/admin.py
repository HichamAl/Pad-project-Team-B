from django.contrib import admin
from .models import UserPoints, Challenge, SecretUser



# Register your models here.
admin.site.register(Challenge)
admin.site.register(UserPoints)
admin.site.register(SecretUser)
