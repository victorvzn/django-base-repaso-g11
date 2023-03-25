from django.urls import path
from .views import ProductsView, ProductView

urlpatterns = [
    path('/products', ProductsView.as_view()),
    path('products/<int:pk>', ProductView.as_view()),
]