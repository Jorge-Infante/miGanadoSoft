from django.contrib import admin
from . models import Species,Animal,Breed

# Register your models here.
admin.site.register(Species)
admin.site.register(Animal)
admin.site.register(Breed)