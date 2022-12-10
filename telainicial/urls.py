
from telainicial.views import index, adocao
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', index),
    path('adocao/', adocao),
    path('form/', views.form, name='form'),
    path('create/', views.create, name='create'),
    path('view/<int:pk>/', views.view, name='view'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
