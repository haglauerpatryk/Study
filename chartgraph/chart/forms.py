from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'num_products']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'num_products': forms.NumberInput(attrs={'class': 'form-control'}),
        }