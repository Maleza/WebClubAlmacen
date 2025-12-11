from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ContenidoIndex, Noticia, Beneficio, BlogPost


# CONFIG de modelos sincronizables → claves homogéneas
SYNC_MODELS = {
    "Noticia": {
        "model": Noticia,
        "titulo": lambda o: o.titulo,
        "descripcion": lambda o: o.contenido[:200],
        "imagen": lambda o: o.imagen.url if o.imagen else "",
        "categoria": "Noticias",
        "link": lambda o: f"/noticias/{o.pk}/",
    },

    "Beneficio": {
        "model": Beneficio,
        "titulo": lambda o: o.titulo,
        "descripcion": lambda o: o.descripcion[:200],
        "imagen": lambda o: o.imagen.url if o.imagen else "",
        "categoria": "Beneficios",
        "link": lambda o: f"/beneficios/{o.pk}/",
    },

    "BlogPost": {
        "model": BlogPost,
        "titulo": lambda o: o.titulo,
        "descripcion": lambda o: o.contenido[:200],   # ← FIX ✔
        "imagen": lambda o: o.imagen.url if o.imagen else "",
        "categoria": "Blog",
        "link": lambda o: f"/blog/{o.pk}/",
    },
}


def sync_index(name, instance):
    """Crear o actualizar un registro en ContenidoIndex sin duplicados"""

    config = SYNC_MODELS[name]

    ContenidoIndex.objects.update_or_create(
        modelo_origen=name,
        objeto_id=instance.pk,
        defaults={
            "titulo": config["titulo"](instance),
            "descripcion": config["descripcion"](instance),
            "imagen": config["imagen"](instance),
            "categoria": config["categoria"],
            "link": config["link"](instance),
        }
    )


def delete_from_index(name, instance):
    ContenidoIndex.objects.filter(
        modelo_origen=name,
        objeto_id=instance.pk
    ).delete()


# ---------- CONECTAR SEÑALES ----------

@receiver(post_save, sender=Noticia)
def noticia_saved(sender, instance, **kwargs):
    sync_index("Noticia", instance)

@receiver(post_delete, sender=Noticia)
def noticia_deleted(sender, instance, **kwargs):
    delete_from_index("Noticia", instance)


@receiver(post_save, sender=Beneficio)
def beneficio_saved(sender, instance, **kwargs):
    sync_index("Beneficio", instance)

@receiver(post_delete, sender=Beneficio)
def beneficio_deleted(sender, instance, **kwargs):
    delete_from_index("Beneficio", instance)


@receiver(post_save, sender=BlogPost)
def blog_saved(sender, instance, **kwargs):
    sync_index("BlogPost", instance)

@receiver(post_delete, sender=BlogPost)
def blog_deleted(sender, instance, **kwargs):
    delete_from_index("BlogPost", instance)
