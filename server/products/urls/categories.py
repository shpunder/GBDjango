from django.urls import path
from products.views import (
    category_detail, category_create, category_update,
    category_delete, category_list
)


app_name = 'categories'


urlpatterns = [
    path('create/', category_create, name='create'),
    path('update/<int:idx>', category_update, name='update'),
    path('delete/<int:idx>', category_delete, name='delete'),
    path('detail/<int:idx>/', category_detail, name='detail'),
    path('', category_list, name='main')
]
