from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmpleadosForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    DNI = forms.IntegerField()

class ProveedoresForm(forms.Form):

    razonsocial = forms.CharField(max_length=30)
    productos = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    email = forms.EmailField()

class ClientesForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fechafactura = forms.DateField()
    telefono = forms.IntegerField()

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget = forms.PasswordInput)

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

