from django import forms
from product_app.models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__" 
