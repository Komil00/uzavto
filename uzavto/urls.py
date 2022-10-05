from django.urls import path, include
from rest_framework import routers

from .views import ModelViewSets, CarsViewSets

router = routers.DefaultRouter()
router.register(r'model', ModelViewSets)
router.register(r'cars', CarsViewSets)
urlpatterns = [
    path('', include(router.urls))
]
