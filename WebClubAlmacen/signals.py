from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.urls import reverse

from .models import (
    Noticia,
    Beneficio,
    BlogPost,
    Streaming,
    ContenidoIndex
)

# ======================================
# CONFIGURACIÓN DEL ÍNDICE
# ======================================

MODELOS = {
    "Noticia": {
        "model": Noticia,
        "categoria": "Noticias",
        "url": lambda obj: reverse("noticia_detalle", args=[obj.pk]),
        "imagen": lambda obj: obj.imagen.url if obj.imagen else None,
        "desc": lambda obj: (obj.contenido or "")[:250],
    },

    "Beneficio": {
        "model": Beneficio,
        "categoria": "Beneficios",
        "url": lambda obj: reverse("beneficio_detalle", args=[obj.pk]),
        "imagen": lambda obj: obj.imagen_ben.url if obj.imagen_ben else None,
        "desc": lambda obj: (obj.descripcion or "")[:250],
    },

    "BlogPost": {
        "model": BlogPost,
        "categoria": "Blog",
        "url": lambda obj: reverse("blog_detalle", args=[obj.pk]),
        "imagen": lambda obj: obj.imagen_blog.url if obj.imagen_blog else None,
        "desc": lambda obj: (obj.contenido or "")[:250],
    },

    "Streaming": {
        "model": Streaming,
        "categoria": "Streaming",
        "url": lambda obj: reverse("streaming_detalle", args=[obj.pk]),
        "imagen": lambda obj: obj.imagen_str.url if obj.imagen_str else None,
        "desc": lambda obj: (obj.descripcion_str or "")[:250],
    },
}


# ======================================
# FUNCIÓN PARA CONECTAR SEÑALES
# ======================================

def conectar_seniales(model, nombre_modelo):

    @receiver(post_save, sender=model)
    def crear_o_actualizar(sender, instance, **kwargs):
        config = MODELOS[nombre_modelo]

        ContenidoIndex.objects.update_or_create(
            modelo_origen=nombre_modelo,
            objeto_id=instance.pk,
            defaults={
                "titulo": getattr(instance, "titulo", ""),
                "descripcion": config["desc"](instance),
                "categoria": config["categoria"],
                "link": config["url"](instance),
                "imagen": config["imagen"](instance),
            },
        )

    @receiver(post_delete, sender=model)
    def eliminar(sender, instance, **kwargs):
        ContenidoIndex.objects.filter(
            modelo_origen=nombre_modelo,
            objeto_id=instance.pk
        ).delete()


# ======================================
# REGISTRAR TODAS LAS SEÑALES
# ======================================

for nombre_modelo, config in MODELOS.items():
    conectar_seniales(config["model"], nombre_modelo)
