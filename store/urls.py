from django.urls import path

from store.views import CategoryAPI

urlpatterns = [
    path("category/", CategoryAPI.as_view(), name="category")
]
