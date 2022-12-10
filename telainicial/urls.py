
from telainicial.views import index, sobre, view, create, noticias, login
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', index),
    path('form/', views.form, name='form'),
    path('sobre/', views.sobre, name='sobre'),
    path('create/', views.create, name='create'),
    path('noticias/', views.noticias, name='noticias'),
    path('login/', views.login, name='login'),
    path('view/<int:pk>/', views.view, name='view'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
