from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # Aditional documentations
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Documentation API
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Admin Django
    path('admin/', admin.site.urls),
    # Products
    path('products/', include("product.urls")),
    #Providers
    path('providers/',include("provider.urls")),
]