from django.db import models
from django import forms


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name} ({self.category.name})"








class UploadFileForm(forms.Form):
    file = forms.FileField()


