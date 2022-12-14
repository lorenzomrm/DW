from django.contrib import admin
from django.urls import path
from telainicial import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('', views.index),
    path('login/', views.login_user),
    path('sobre/', views.sobre, name='sobre'),
    path('noticias/', views.noticias, name='noticias'),
    path('login/submit', views.submit_login),
    path('pet/user/', views.list_user_pets),
    path('pet/all/', views.list_all_pets),
    path('pet/detail/<slug:id>/', views.pet_detail),
    path('pet/register/', views.register_pet),
    path('noticia/register/', views.register_noticia),
    path('noticia/register/submit', views.set_noticia),
    path('pet/register/submit', views.set_pet),
    path('pet/delete/<slug:id>/', views.delete_pet),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url='pet/all/')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
