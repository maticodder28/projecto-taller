from django import forms
from tiendaApp.models import Productos, TipoUsuario, Mesas, Usuarios, Comanda, DetalleComanda, Categoria

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

class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UsuarioForm(forms.ModelForm):
    # Define el campo tipoUsuario manualmente
    tipoUsuario = forms.ModelChoiceField(
        queryset=TipoUsuario.objects.all(),  # Recupera todos los objetos TipoUsuario
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'rut', 'email', 'password', 'password2', 'telefono', 'tipoUsuario', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            # No es necesario definir un widget para 'tipoUsuario' aquí ya que ya lo definiste arriba
        }

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesas
        fields = ['numero', 'estado']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

class ComandaForm(forms.ModelForm):
    class Meta:
        model = Comanda
        fields = ['fecha', 'productos', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'productos': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

