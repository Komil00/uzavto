from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from .serializers import CustomUserSerializers
from .models import CustomUser

from rest_framework import permissions

from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     if obj.author == request.user:
    #         return True
    #     return False


# @csrf_exempt
# @api_view()
# def hello_world(request):
#     if request.method == 'GET':
#         users = CustomUser.objects.all()
#         doc_serializer = CustomUserSerializers(users, many=True)
#         return JsonResponse(doc_serializer.data, safe=False)
#     elif request.method == 'POST':
#         doc_data = JSONParser().parse(request)
#         doc_serializer = CustomUserSerializers(data=doc_data)
#         if doc_serializer.is_valid():
#             doc_serializer.save()
#             return JsonResponse(doc_serializer.data, status=201)
#         return JsonResponse(doc_serializer.errors, status=400)


class UsersViewCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = CustomUserSerializers(queryset, many=True)
    #     return Response(serializer.data)


class UsersViewList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers

# class UserView(generics.RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#
#     def perform_update(self, serializer):
#         if self.request.user.is_staff:
#             instance = self.get_object()
#             serializer.save(instance=instance)
#         if self.request.user.role == 'MANAGER':
#             user = CustomUser.objects.get(pk=self.kwargs['pk'])
#             if user.role == 'OPERATOR':
#                 instance = self.get_object()
#                 serializer.save(instance=instance)
#             else:
#                 return None


# class AccountView(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = AccountSerializer
