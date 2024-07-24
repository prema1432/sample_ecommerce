from django.urls import path

from store.views import CategoryAPI, CategoryDetailAPI, ProductAPI, OrderAPI

urlpatterns = [
    path("category/", CategoryAPI.as_view(), name="category"),
    path("category/<str:pk>/", CategoryDetailAPI.as_view(), name="category_detail"),
    path("products/", ProductAPI.as_view(), name="product"),
    path('orders/', OrderAPI.as_view(), name="order"),
]
