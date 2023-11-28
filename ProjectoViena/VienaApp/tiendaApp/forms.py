from django import forms
from tiendaApp.models import Productos, Mesas, UserProfile, Comanda, DetalleComanda, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re


class ProductoForm(forms.ModelForm):
    # Agrega un campo para la categoría que recupera las categorías desde la base de datos
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),  # Este queryset obtiene todas las categorías
        required=False,  # Puedes hacer que este campo no sea obligatorio si lo deseas
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione una categoría"  # Texto para la opción vacía (opcional)
        
    )

    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesas
        fields = ['numero']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DetalleComandaForm(forms.ModelForm):
    class Meta:
        model = DetalleComanda
        fields = ['producto', 'cantidad']

class NewUserForm(UserCreationForm):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    CARGO_CHOICES = [
        ('Encargado', 'Encargado'),
        ('Cajero', 'Cajero'),
        ('Garzon', 'Garzón'),
        ('Cocinero', 'Cocinero'),
    ]
    cargo = forms.ChoiceField(choices=CARGO_CHOICES)
    rut = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "nombre", "apellido", "cargo", "rut")

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        rut = rut.replace('.', '').replace('-', '')
        cuerpo, dv = rut[:-1], rut[-1].upper()

        # Validar que el cuerpo tenga 7 o más dígitos y que el DV sea un dígito o 'K'
        if not cuerpo.isdigit() or len(cuerpo) < 7 or (dv != 'K' and not dv.isdigit()):
            raise forms.ValidationError("RUT inválido.")

        # Calcular dígito verificador
        suma = sum([int(digit) * int('32765432'[i % 8]) for i, digit in enumerate(reversed(cuerpo))])
        dv_esperado = '0' if suma % 11 == 0 else 'K' if suma % 11 == 1 else str(11 - suma % 11)

        if dv != dv_esperado:
            raise forms.ValidationError("RUT inválido. Dígito verificador no coincide.")

        return rut

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user_profile = UserProfile(user=user, nombre=self.cleaned_data["nombre"], 
                                       apellido=self.cleaned_data["apellido"], 
                                       cargo=self.cleaned_data["cargo"], 
                                       rut=self.cleaned_data["rut"])
            user_profile.save()
        return user
    
