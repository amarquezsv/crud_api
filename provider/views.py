import django_filters.rest_framework
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from .models import Providers
from .serializers import ProvidersSerializer

# All Providers
class ListProviders(generics.ListAPIView):
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer
    #The API should also provide the following features:
    #c. Order by property
    #d. Filtering by property (Providers)
    filter_backends = [OrderingFilter]

# Detail Provider
class DetailProvider(generics.RetrieveAPIView):
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer
# Update Provider
class ProviderUpdateView(generics.UpdateAPIView):
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer
# Delete Provider
class ProviderDeleteView(generics.DestroyAPIView):
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer
# Create Provider
class ProviderCreate(generics.ListCreateAPIView):
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer