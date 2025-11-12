from django import forms
from .models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = Usuario
        fields = ['nombre', 'apaterno', 'amaterno', 'email', 'contrasena', 'tipo_usuario']

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
    