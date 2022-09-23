import attrs as attrs
from django import forms
from django.forms import ModelForm

from Aplicacion.cuenta_cobrar.models import Cabecera,PagoDeuda


class CabeceraForm(ModelForm):
    class Meta:
        model = Cabecera
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control '}),
            'deuda': forms.NumberInput(attrs={'class':'form-control'}),
            'fecha_cobro': forms.DateInput(format=('%d/%m/%Y'),
                                    attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),

            'cuota_mensual':forms.NumberInput(attrs={'class':'form-control','readonly':True})
        }


class PagoDeudaForm(ModelForm):
    class Meta:
        model = PagoDeuda
        fields = '__all__'
        exclude = ['deuda']
        widgets = {
            'abono':forms.NumberInput(attrs= {'placeholder': 'Ingrese el valor de pago','class':'form-control'}),
            'fecha_ab': forms.DateInput(format=('%d/%m/%Y'),
                                        attrs={'class': 'form-control', 'type': 'date'}),
            'cabecera':forms.Select(attrs={'class':'form-control'})
        }