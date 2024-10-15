from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Medicines'
    
    def __str__(self) -> str:
        return str(self.id)+ 'Nombre: '+self.name 

class Treatment(models.Model):
    name = models.CharField(max_length=50)
    medicine = models.ManyToManyField(Medicine, blank=True)
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Treatments'

    def __str__(self) -> str:
        return str(self.id)+ 'Nombre: '+self.name 