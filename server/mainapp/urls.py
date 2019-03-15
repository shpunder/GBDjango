from django.urls import path


from .views import (
    main, about, contacts
)

app_name = 'main'

urlpatterns = [
    path('contacts/', contacts, name = 'contacts'),
    path('about/', about, name = 'about'),
    path('', main, name = 'main'),
]