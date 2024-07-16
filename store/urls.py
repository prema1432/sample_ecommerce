from django.urls import path

from store.views import CategoryAPI, CategoryDetailAPI

urlpatterns = [
    path("category/", CategoryAPI.as_view(), name="category"),
    path("category/<str:pk>/", CategoryDetailAPI.as_view(), name="category_detail"),
]
