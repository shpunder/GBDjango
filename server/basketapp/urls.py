from django.urls import path
from basketapp.views import (basket_add, basket_detail, basket_remove)


app_name = 'basketapp'


urlpatterns = [
    path('', basket_detail, name='detail'),
    path('add/<int:idx>', basket_add, name='add'),
    path('remove/<int:idx>)', basket_remove, name='remove'),
]
