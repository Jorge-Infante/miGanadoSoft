from django.contrib import admin
from . models import Species,Animal,Breed, Status

# Register your models here.
admin.site.register(Species)
admin.site.register(Animal)
admin.site.register(Breed)
admin.site.register(Status)