from django.db import models
from django import forms


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(
        blank=True,
        null=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='products',
        blank=True,
        null=True)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE)
    description = models.TextField(
        blank=True,
        null=True)
    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0)
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )


    def __str__(self):
        return f"{self.name} ({self.category.name})"


class UploadFileForm(forms.Form):
    file = forms.FileField()
