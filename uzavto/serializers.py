from rest_framework import serializers
from .models import Cars, Model


class ModelListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class CarsListSerializers(serializers.ModelSerializer):
    model = ModelListSerializers()

    class Meta:
        model = Cars
        fields = ['model', 'name', 'year', 'image', 'expenses', 'color', 'price']


class CarsPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = ['model', 'name', 'year', 'image', 'expenses', 'color', 'price']