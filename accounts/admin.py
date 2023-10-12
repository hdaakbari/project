from django.contrib import admin
from accounts.models import *
from .models import UserProfile,Education,Experience

admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Experience)