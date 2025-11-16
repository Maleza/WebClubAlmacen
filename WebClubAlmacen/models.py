from django.db import models
from django.utils import timezone


# Create your models here.
class Usuario(models.Model):
    
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128, null=True,blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=300)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_publicacion']

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.titulo

class Streaming(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    url = models.URLField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Beneficio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='beneficios/', blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class EnlaceUtil(models.Model):
    categoria = models.CharField(max_length=100, blank=True)
    nombre = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.nombre

class Invitacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_evento = models.DateField()

    def __str__(self):
        return self.titulo

class NuevoComercio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to='comercios/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class RedSocial(models.Model):
    plataforma = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.plataforma

class Reunion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.titulo

class Directorio(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=250, blank=True)
    correo = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre