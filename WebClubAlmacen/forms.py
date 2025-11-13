from django import forms
from .models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = Usuario
        fields = ['nombre', 'apaterno', 'amaterno', 'email', 'contrasena', 'tipo_usuario']
        #etiquetas que se renderizan en el formulario de registro de usuario
        labels = {
            'nombre': 'Nombre',
            'apaterno': 'Apellido Paterno',
            'amaterno': 'Apellido Materno',
            'email': 'Correo Electrónico',
            'contrasena': 'Contraseña',
            'tipo_usuario': 'Tipo de Usuario',
        }
        widgets = {
            'contrasena': forms.PasswordInput(attrs={'placeholder': 'Escribe tu contraseña'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'apaterno': forms.TextInput(attrs={'placeholder': 'Tu apellido paterno'}),
            'amaterno': forms.TextInput(attrs={'placeholder': 'Tu apellido materno'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            'tipo_usuario': forms.TextInput(attrs={'placeholder': 'Administrador / Comerciante / Proveedor'}),
        }
    def clean_contrasena(self):
        pwd = self.cleaned_data.get('contrasena')
        # valida seguridad mínima opcional
        if pwd and len(pwd) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return pwd

    def save(self, commit=True):
        instance = super().save(commit=False)
        raw = self.cleaned_data.get('contrasena')
        if raw:
            instance.contrasena = make_password(raw)   # hash
        if commit:
            instance.save()
        return instance
    