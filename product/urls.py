from django.urls import path
from .views import ListProducts, DetailProduct,ProductCreate,ProductDeleteView,ProductUpdateView

urlpatterns = [
    # Detail Product
    path("<int:pk>/", DetailProduct.as_view(), name="product_detail"),
    # All Products
    path("", ListProducts.as_view(), name="products_list"),
    # Create Product
    path('create/', ProductCreate.as_view(), name='product_create'),
    # Update Product
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    # Delete Product
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_destroy'),
]