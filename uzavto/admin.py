from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cars, Model


# Register your models here.

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('model',)
    # fields = ['model', 'name', 'year', 'image']
    list_display = ['name', 'model', 'price']


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)
    # fields = ['model', 'name', 'year', 'image']
    list_display = ['name', ]
