from django.contrib import admin
from .models import Usuario,Comentario
# Register your models here.

admin.site.site_header = "Web Club Almacen Admin"
admin.site.register(Usuario)
admin.site.register(Comentario)