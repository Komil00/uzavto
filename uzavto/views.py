from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from customuser.serializers import UserSerializer
from .models import Cars, Model
from rest_framework import viewsets, status
from .serializers import ModelListSerializers, CarsListSerializers, CarsPostSerializers


class CarsViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['model']
    search_fields = ['name']
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, serializer_class=CarsPostSerializers, permission_classes=[IsAdminUser], methods=['post'], )
    def add_cars(self, request, pk):
        serializer = CarsPostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ModelViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelListSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, permission_classes=[IsAdminUser], methods=['post'])
    def add_models(self, request):
        serializer = ModelListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'created'}, )
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
