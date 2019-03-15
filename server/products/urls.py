from django.urls import path


from .views import (
    product_detail, products_list
)

app_name = 'products'

urlpatterns = [
    path('detail/', product_detail, name = 'detail'),
    path('', products_list, name = 'main'),
]