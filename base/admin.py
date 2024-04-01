from django.contrib import admin
from .models import Booking, UserProfile

# TODO: decide if I want to use admin

admin.site.register(Booking)
admin.site.register(UserProfile)

# TODO: if using admin, add more functionality
