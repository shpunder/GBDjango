from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('categories/', include('products.urls.categories')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('', include('mainapp.urls')),
    path('auth/', include('authapp.urls', namespace='auth'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
