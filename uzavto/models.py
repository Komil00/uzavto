from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe

from customuser.models import CustomUser


# Create your models here.

class Model(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=False, null=False)
    logo = models.ImageField(blank=False, null=False, upload_to='model')

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return self.name


class Cars(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(unique=True, max_length=30, blank=False, null=False)
    year = models.DateField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False, upload_to='cars')
    expenses = models.FloatField(blank=False, null=False)  # rasxod
    color = models.CharField(max_length=30, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name
