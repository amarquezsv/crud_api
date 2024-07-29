from django.urls import path
from .views import ListProviders, DetailProvider,ProviderUpdateView,ProviderDeleteView,ProviderCreate

urlpatterns = [
    # Detail Provider
    path("<int:pk>/", DetailProvider.as_view(), name="provider_detail"),
    # All Providers
    path("", ListProviders.as_view(), name="providers_list"),
    # Create Provider
    path('create/', ProviderCreate.as_view(), name='provider_create'),
    # Update Provider
    path('<int:pk>/update/', ProviderUpdateView.as_view(), name='provider_update'),
    # Delete Provider
    path('<int:pk>/delete/', ProviderDeleteView.as_view(), name='provider_destroy'),
]
