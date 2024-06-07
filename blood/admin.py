from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Blood_Donation)
admin.site.register(Order)