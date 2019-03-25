from django.urls import path
from .views import (
    product_list, product_detail, upload_file, category_detail,
    category_create
)


app_name = 'products'


urlpatterns = [
    path('create', category_create, name='create'),
    path('<int:idx>/', product_detail, name='detail'),
    path('category/<int:idx>/', category_detail, name='category'),
    path('', product_list, name='main'),
    path('load', upload_file, name='load'),
]
