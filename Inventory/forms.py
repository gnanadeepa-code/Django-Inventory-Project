#from django.forms import ModelForm
from django import forms
from .models import *

class Inventory_ItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields ='__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 3}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '    Enter amount'}),
            'gst': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter GST percentage'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }