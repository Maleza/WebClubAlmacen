"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WebClubAlmacen import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_html, name='index'),
    path('login/', views.login_html, name='login'),
    path('noticias/', views.noticias_html, name='noticias'),
    path('blog/', views.blog_html, name='blog'),
    path('streaming/', views.streaming_html, name='streaming'),
    path('beneficios/', views.beneficios_html, name='beneficios'),
    path('enlaces_utiles/', views.enlaces_utiles_html, name='enlaces_utiles'),
    path('invitaciones/', views.invitaciones_html, name='invitaciones'),
    path('nuevos_comercios/', views.nuevos_comercios_html, name='nuevos_comercios'),
    path('redes_sociales/', views.redes_sociales_html, name='redes_sociales'),
    path('reunion/', views.reunion_html, name='reunion'),
    path('streaming/', views.streaming_html, name='streaming'),
    path('directorio/', views.directorio_html, name='directorio'),
]
