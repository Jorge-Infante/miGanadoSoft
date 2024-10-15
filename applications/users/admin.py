from django.contrib import admin
from . models import User, Company

admin.site.register(Company)
admin.site.register(User)