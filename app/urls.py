from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('product/<int:pk>/highlight/', views.ProductDetail.as_view(), name='product-highlight'),
    path('cart/', views.CartList.as_view()),
    path('cart/<int:pk>/', views.CartList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
