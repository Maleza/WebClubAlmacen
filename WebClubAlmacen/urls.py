from django.urls import path
from WebClubAlmacen import views
from .views import UsuarioLoginView

urlpatterns = [
    path('', views.index_html, name='index'),

    # -----------------------------
    # AUTENTICACIÓN
    # -----------------------------
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_html, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # -----------------------------
    # NOTICIAS
    # -----------------------------
    path('noticias/', views.noticias_html, name='noticias'),
    path('noticias/crear/', views.noticia_crear, name='noticia_crear'),
    path('noticias/<int:pk>/', views.noticia_detalle, name='noticia_detalle'),
    path('noticias/editar/<int:pk>/', views.noticia_editar, name='noticia_editar'),
    path('noticias/eliminar/<int:pk>/', views.noticia_eliminar, name='noticia_eliminar'),

    # -----------------------------
    # BLOG
    # -----------------------------
    path('blog/', views.blog_html, name='blog'),
    path('blog/crear/', views.blog_crear, name='blog_crear'),
    path('blog/<int:pk>/', views.blog_detalle, name='blog_detalle'),
    path('blog/editar/<int:pk>/', views.blog_editar, name='blog_editar'),
    path('blog/eliminar/<int:pk>/', views.blog_eliminar, name='blog_eliminar'),

    # -----------------------------
    # STREAMING
    # -----------------------------
    path('streaming/', views.streaming_html, name='streaming'),
    path('streaming/crear/', views.streaming_crear, name='streaming_crear'),
    path('streaming/<int:pk>/', views.streaming_detalle, name='streaming_detalle'),
    path('streaming/editar/<int:pk>/', views.streaming_editar, name='streaming_editar'),
    path('streaming/eliminar/<int:pk>/', views.streaming_eliminar, name='streaming_eliminar'),

    # -----------------------------
    # BENEFICIOS
    # -----------------------------
    path('beneficios/', views.beneficios_html, name='beneficios'),
    path('beneficios/crear/', views.beneficio_crear, name='beneficio_crear'),
    path('beneficios/<int:pk>/', views.beneficio_detalle, name='beneficio_detalle'),
    path('beneficios/editar/<int:pk>/', views.beneficio_editar, name='beneficio_editar'),
    path('beneficios/eliminar/<int:pk>/', views.beneficio_eliminar, name='beneficio_eliminar'),

    # -----------------------------
    # ENLACES ÚTILES
    # -----------------------------
    path('enlaces_utiles/', views.enlaces_utiles_html, name='enlaces_utiles'),
    path('enlaces_utiles/crear/', views.enlace_crear, name='enlace_crear'),
    path('enlaces_utiles/<int:pk>/', views.enlace_detalle, name='enlace_detalle'),
    path('enlaces_utiles/editar/<int:pk>/', views.enlace_editar, name='enlace_editar'),
    path('enlaces_utiles/eliminar/<int:pk>/', views.enlace_eliminar, name='enlace_eliminar'),

    # -----------------------------
    # INVITACIONES
    # -----------------------------
    path('invitaciones/', views.invitaciones_html, name='invitaciones'),
    path('invitaciones/crear/', views.invitacion_crear, name='invitacion_crear'),
    path('invitaciones/<int:pk>/', views.invitacion_detalle, name='invitacion_detalle'),
    path('invitaciones/editar/<int:pk>/', views.invitacion_editar, name='invitacion_editar'),
    path('invitaciones/eliminar/<int:pk>/', views.invitacion_eliminar, name='invitacion_eliminar'),

    # -----------------------------
    # NUEVOS COMERCIOS
    # -----------------------------
    path('nuevos_comercios/', views.nuevos_comercios_html, name='nuevos_comercios'),
    path('nuevos_comercios/crear/', views.nuevo_comercio_crear, name='comercio_crear'),
    path('nuevos_comercios/<int:pk>/', views.nuevo_comercio_detalle, name='comercio_detalle'),
    path('nuevos_comercios/editar/<int:pk>/', views.nuevo_comercio_editar, name='comercio_editar'),
    path('nuevos_comercios/eliminar/<int:pk>/', views.nuevo_comercio_eliminar, name='comercio_eliminar'),

    # -----------------------------
    # REDES SOCIALES
    # -----------------------------
    path('redes_sociales/', views.redes_sociales_html, name='redes_sociales'),
    path('redes_sociales/crear/', views.red_social_crear, name='redsocial_crear'),
    path('redes_sociales/<int:pk>/', views.red_social_detalle, name='redsocial_detalle'),
    path('redes_sociales/editar/<int:pk>/', views.red_social_editar, name='redsocial_editar'),
    path('redes_sociales/eliminar/<int:pk>/', views.red_social_eliminar, name='redsocial_eliminar'),

    # -----------------------------
    # REUNIONES
    # -----------------------------
    path('reuniones/', views.reuniones_html, name='reuniones'),
    path('reuniones/crear/', views.reunion_crear, name='reunion_crear'),
    path('reuniones/<int:pk>/', views.reunion_detalle, name='reunion_detalle'),
    path('reuniones/editar/<int:pk>/', views.reunion_editar, name='reunion_editar'),
    path('reuniones/eliminar/<int:pk>/', views.reunion_eliminar, name='reunion_eliminar'),

    # -----------------------------
    # DIRECTORIO
    # -----------------------------
    path('directorio/', views.directorio_html, name='directorio'),
    path('directorio/crear/', views.directorio_crear, name='directorio_crear'),
    path('directorio/<int:pk>/', views.directorio_detalle, name='directorio_detalle'),
    path('directorio/editar/<int:pk>/', views.directorio_editar, name='directorio_editar'),
    path('directorio/eliminar/<int:pk>/', views.directorio_eliminar, name='directorio_eliminar'),

    # -----------------------------
    # ASISTENTE IA
    # -----------------------------
    path('asistente_IA/', views.asistente_IA_html, name='asistente_IA'),
]
