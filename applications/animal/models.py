from django.db import models
from applications.treatment.models import Treatment


class Species(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Especie'
    def __str__(self) -> str:
        return str(self.id)+self.name
    
class Breed(models.Model):
    name = models.CharField(max_length=50)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, null=False)
    def __str__(self) -> str:
        return str(self.id) + self.name

class Animal(models.Model):
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    species = models.ForeignKey(Species, on_delete=models.CASCADE, null=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=False)
    treatment = models.ManyToManyField(Treatment, blank=True, null=True)
    file = models.FileField(upload_to='uploads/',null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self) -> str:
        return str(self.id)+self.name

