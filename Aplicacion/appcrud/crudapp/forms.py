from django import forms
from .models import Tablaagenda


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Tablaagenda
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingrese Nombre"}
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingrese Apellido"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Ingrese Email"}
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingrese Telefono"}
            ),
            "direccion": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingrese Direccion"}
            ),
        }