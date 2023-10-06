from django.contrib import admin
from accounts.models import *
from .models import UserProfile

admin.site.register(UserProfile)