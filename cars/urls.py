from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uzavto.urls')),
    path('users/', include('customuser.urls')),

    path('api/', include('rest_framework.urls')),
    path('swagger-docs/', schema_view),
    path('docs/', include_docs_urls(title='Polls API')),
]
