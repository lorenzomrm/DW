
from telainicial.views import index, adocao
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('adocao/', adocao)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
