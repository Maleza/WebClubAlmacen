from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("El superusuario debe tener is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True")

        return self.create_user(email, password, **extra_fields)
# Modelo de Atenticacion de Usuario  Heredando  de Django 
class Usuario(AbstractUser):
    username = None  
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=30, choices=[
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('lector', 'Lector'),
    ], default='lector')

    objects = UserManager()  


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
    


class DashboardItem(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

# Modelo para el contenido del índex principal

class ContenidoIndex(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="index/", null=True, blank=True)
    categoria = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    # Para identificar desde qué modelo viene (Noticia, Beneficio, Blog, etc)
    modelo_origen = models.CharField(max_length=100)
    objeto_id = models.IntegerField()

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return f"{self.categoria}: {self.titulo}"
