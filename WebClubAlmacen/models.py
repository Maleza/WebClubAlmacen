from django.db import models

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