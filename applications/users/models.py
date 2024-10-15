from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Company(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
    )

    def __str__(self):
        return self.username


