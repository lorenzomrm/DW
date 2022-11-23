
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('telainicial.urls')),
    path('index', include('telainicial.urls')),
    path('adocao', include('telainicial.urls')),
]
