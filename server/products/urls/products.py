from django.urls import path
from products.views import (
    product_list, product_detail, upload_file,
)


app_name = 'products'


urlpatterns = [
    path('<int:idx>/', product_detail, name='detail'),
    path('', product_list, name='main'),
    path('load', upload_file, name='load'),
]
