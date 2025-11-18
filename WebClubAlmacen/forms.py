from django import forms
from .models import * 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


#Formulario de registro de usuarios
Usuario = get_user_model()

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ["email", "nombre", "apaterno", "amaterno", "tipo_usuario"]

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
#Formulario de Login de Usuarios


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Correo o Usuario",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu nombre de usuario"
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "**********"
        })
    )





#Formulario de Comentarios
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'contenido']  # o ['nombre', 'tema', 'contenido'] si agregaste el campo tema
        labels = {
            'nombre': 'Tu nombre',
            'contenido': 'Comentario',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Escribe tu nombre',
                'class': 'input-text'
            }),
            'contenido': forms.Textarea(attrs={
                'placeholder': 'Escribe tu comentario aquí...',
                'class': 'textarea-box',
                'rows': 4
            }),
        }

#Formulario de Noticias
class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'autor']
        labels = {
            'titulo': 'Título',
            'resumen': 'Resumen breve',
            'contenido': 'Contenido completo',
            'imagen': 'Imagen destacada',
            'autor': 'Autor',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la noticia'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Resumen corto'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Contenido completo'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del autor'}),
        }


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

class StreamingForm(forms.ModelForm):
    class Meta:
        model = Streaming
        fields = '__all__'

class BeneficioForm(forms.ModelForm):
    class Meta:
        model = Beneficio
        fields = '__all__'

class EnlaceUtilForm(forms.ModelForm):
    class Meta:
        model = EnlaceUtil
        fields = '__all__'

class InvitacionForm(forms.ModelForm):
    class Meta:
        model = Invitacion
        fields = '__all__'

class NuevoComercioForm(forms.ModelForm):
    class Meta:
        model = NuevoComercio
        fields = '__all__'

class RedSocialForm(forms.ModelForm):
    class Meta:
        model = RedSocial
        fields = '__all__'

class ReunionForm(forms.ModelForm):
    class Meta:
        model = Reunion
        fields = '__all__'

class DirectorioForm(forms.ModelForm):
    class Meta:
        model = Directorio
        fields = '__all__'