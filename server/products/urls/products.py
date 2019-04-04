from django.urls import path
from products.views import (
    product_list, product_detail, upload_file,
    product_create, product_update, product_delete,
    product_rest_list, ProductCreate, ProductUpdate,
    ProductDelete, ProductList, ProductDetail
)


app_name = 'products'


urlpatterns = [
    path('create/', ProductCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='main'),
    path('load', upload_file, name='load'),
]

urlpatterns += [
    path('api/', product_rest_list, name='rest_list')
]
