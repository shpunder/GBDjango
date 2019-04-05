from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('categories/', include('products.urls.categories')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('', include('mainapp.urls')),
    path('auth/', include('authapp.urls', namespace='auth'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
