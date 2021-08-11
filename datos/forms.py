from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django.db import models 
from datos.models import Cliente_corral, Contenedores_Mat_prima, Contenedores_Producto, Materia_prima, Operador, Provedor, Tipo_animal, Unidad, registro, Corral, Producto,Cliente
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
		help_texts = {k:"" for k in fields }

class formulario(forms.ModelForm):
    class Meta:
        model = registro
        fields = '__all__'
        widgets = {'fecha':  forms.DateInput(attrs={'type': 'date'}),  
}
# , 'corral': AutocompleteSelect(
#             registro._meta.get_field('corral').remote_field, admin.site, attrs={'placeholder': 'seleccionar...'},
#         ), 'producto': AutocompleteSelect(
#             registro._meta.get_field('producto').remote_field, admin.site, attrs={'placeholder': 'seleccionar...'})
#    
class corral(forms.ModelForm):
    class Meta:
        model = Corral
        fields = '__all__'      
        widgets = {'fecha':  forms.DateInput(attrs={'type': 'date'}), 'cliente':forms.HiddenInput()}  

class producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  
        widgets = {'fecha':  forms.DateInput(attrs={'type': 'date'})}  

class cliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  
        widgets = {'fecha':  forms.DateInput(attrs={'type': 'date'})}    

class provedor(forms.ModelForm):
    class Meta:
        model = Provedor
        fields = '__all__'  
        widgets = {'fecha':  forms.DateInput(attrs={'type': 'date'})}   
  
class operador(forms.ModelForm):
    class Meta:
        model = Operador
        fields = '__all__' 
        # widgets = {
        # 'nombre': forms.HiddenInput()}

class tipo_animal(forms.ModelForm):
    class Meta:
        model = Tipo_animal
        fields = '__all__' 

class unidad(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = '__all__' 

class materia_prima(forms.ModelForm):
    class Meta:
        model = Materia_prima
        fields = '__all__' 

class contenedores_mat_prima(forms.ModelForm):
    class Meta:
        model = Contenedores_Mat_prima
        fields = '__all__' 

class contenedores_producto(forms.ModelForm):
    class Meta:
        model = Contenedores_Producto
        fields = '__all__' 


class cliente_corral(forms.ModelForm):
    class Meta:
        model = Cliente_corral
        fields = '__all__' 