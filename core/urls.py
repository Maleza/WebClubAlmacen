
from django.contrib import admin
from django.urls import path
from WebClubAlmacen import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_html, name='index'),
    path('login/', views.login_html, name='login'),
    path('noticias/', views.noticias_html, name='noticias'),
    path('noticias/<int:pk>/', views.noticia_detalle, name='noticia_detalle'),
    path('noticias/crear/', views.noticia_crear, name='noticia_crear'),
    path('noticias/editar/<int:pk>/', views.noticia_editar, name='noticia_editar'),
    path('noticias/eliminar/<int:pk>/', views.noticia_eliminar, name='noticia_eliminar'),
    path('blog/', views.blog_html, name='blog'),
    path('streaming/', views.streaming_html, name='streaming'),
    path('beneficios/', views.beneficios_html, name='beneficios'),
    path('enlaces_utiles/', views.enlaces_utiles_html, name='enlaces_utiles'),
    path('invitaciones/', views.invitaciones_html, name='invitaciones'),
    path('nuevos_comercios/', views.nuevos_comercios_html, name='nuevos_comercios'),
    path('redes_sociales/', views.redes_sociales_html, name='redes_sociales'),
    path('reuniones/', views.reunion_html, name='reuniones'),
    path('streaming/', views.streaming_html, name='streaming'),
    path('directorio/', views.directorio_html, name='directorio'),
    path('registro/', views.registro_usuario, name='registro'),
    path('asistente_IA/', views.asistente_IA_html, name='asistente_IA'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)