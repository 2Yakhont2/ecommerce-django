from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre completo'}), required=True)
    shipping_departments = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Departamento'}), required=True)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad'}), required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección 1'}), required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección 2'}), required=False)
    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_departments', 'shipping_city', 'shipping_address1', 'shipping_address2']

        # Excluir el campo usuario del formulario de envio
        exclude = ['user',]
