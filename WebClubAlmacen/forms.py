from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Tipos de usuario disponibles
TIPOS_USUARIO = [
    ('administrador', 'Administrador'),
    ('comerciante', 'Comerciante'),
    ('proveedor', 'Proveedor'),
]

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIO, label="Tipo de usuario")

    class Meta:
        model = User
        fields = ['username', 'email', 'tipo_usuario', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con este correo.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        # Guardamos tipo de usuario en el campo 'first_name' como ejemplo (puedes crear un perfil aparte)
        user.first_name = self.cleaned_data['tipo_usuario']
        if commit:
            user.save()
        return user
