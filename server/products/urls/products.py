from django.urls import path
from products.views import (
    product_list, product_detail, upload_file,
    product_create, product_update, product_delete,
    product_rest_list
)


app_name = 'products'


urlpatterns = [
    path('create/', product_create, name='create'),
    path('update/<int:idx>/', product_update, name='update'),
    path('delete/<int:idx>/', product_delete, name='delete'),
    path('<int:idx>/', product_detail, name='detail'),
    path('', product_list, name='main'),
    path('load', upload_file, name='load'),
]

urlpatterns += [
    path('api/', product_rest_list, name='rest_list')
]
