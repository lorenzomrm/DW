
from django.contrib import admin
from django.urls import path, include
from telainicial import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('telainicial.urls')),
    path('index', include('telainicial.urls')),
    path('adocao', include('telainicial.urls')),
    url(r'^adoptions/(\d+)/', views.pet_detial, name='pet_detail'),
]
