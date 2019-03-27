from django import forms
from products.models import ProductCategory


class ProductCategoryForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-field'}
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-field'}
        )
    )

class ProductCategoryModelForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']
        widgets = {
            'name': forms.widgets.TextInput(
                attrs={'class': 'form-field'}
            ),
            'description': forms.widgets.Textarea(
                attrs={'class': 'form-field'}
            )
        }
