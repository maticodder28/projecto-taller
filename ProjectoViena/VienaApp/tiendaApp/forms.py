from django import forms
from tiendaApp.models import Productos, Mesas, UserProfile, Comanda, DetalleComanda, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
    
