from django.contrib import admin
from .models import Usuario,Comentario,Noticia
# Register your models here.

admin.site.site_header = "Web Club Almacen Admin"
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Noticia)
