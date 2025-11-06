from django.db import models

# Create your models here.
class usuario(models.Model):
    usuario = models.AutoField(primary_key=True)
    contraseña = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre