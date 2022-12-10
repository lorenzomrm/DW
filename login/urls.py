from django.urls import path
from login import views

urlpatterns = [
    path('registration/register.html',views.NovaConta.as_view(),name='signup')
]