from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(LocationSet)
admin.site.register(Location)

# Register your models here.
