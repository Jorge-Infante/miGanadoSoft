from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Medicamentos'
    
    def __str__(self) -> str:
        return str(self.id)+ 'Nombre: '+self.name 

class Treatment(models.Model):
    name = models.CharField(max_length=50)
    medicine = models.ManyToManyField(Medicine, blank=True, null=True)
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Tratamientos'

    def __str__(self) -> str:
        return str(self.id)+ 'Nombre: '+self.name 