from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "Web Club Almacen Admin"
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Noticia)
admin.site.register(BlogPost)
admin.site.register(Streaming)
admin.site.register(Beneficio)
admin.site.register(EnlaceUtil)
admin.site.register(Invitacion)
admin.site.register(NuevoComercio)
admin.site.register(RedSocial)
admin.site.register(Reunion)
admin.site.register(Directorio)
