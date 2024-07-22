# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Category, Product
from store.serializers import CategorySerilizers, ProductSerilizers, ProductSerilizersPOST


class CategoryAPI(APIView):

    def get(self, request):

        # from faker import Faker
        #
        # from store.models import Category
        #
        # no_of_catgories = 100
        # fake = Faker()
        #
        # for i in range(no_of_catgories):
        #     category = Category()
        #     category.name = fake.word()
        #     category.description = fake.text()
        #     category.save()
        #

        name = request.query_params.get("name", None)

        category = Category.objects.all()

        if name is not None:
            # category = category.filter(name=name) Excat name
            # category = category.filter(name__icontains=name) # its case sensitive
            category = category.filter(name__icontains=name)  # its case sensitive

        # pagination
        # paginator = PageNumberPagination()
        # paginator.page_size = 18

        paginator = LimitOffsetPagination()
        category = paginator.paginate_queryset(category, request)

        # categoryi = paginator.paginate_queryset(category, request)

        serializer = CategorySerilizers(category, many=True)
        # return Response({"data": serializer.data})
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        print("request", request)
        print("request data", request.data)
        categories = CategorySerilizers(data=request.data)
        if categories.is_valid():
            categories.save()
            return Response(categories.data)
        else:
            return Response(categories.errors)


class CategoryDetailAPI(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerilizers(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerilizers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def patch(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerilizers(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def pos


# function based
# 1. function - 1 endpooint
# users- list of users
# create_user
# update_user
# delte userr

# Class
# get -all the data, retrivve
# post - creating
# put - all the fields
# patch - partial upodat
# delete - delete
#
# get - id- all()
# post -
# put , patch - delete - id

class ProductAPI(APIView):

    def get(self, request):
        name = request.query_params.get("name", None)
        id = request.query_params.get("id", None)
        products = Product.objects.all()
        if name is not None:
            products = products.filter(name__icontains=name)
        if id is not None:
            try:
                products = products.get(id=id)
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = ProductSerilizers(products)
            return Response(serializer.data)

        serializer = ProductSerilizers(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        if data.get("category") is not None:
            if type(data.get("category")) == int:
                try:
                    data["category"] = Category.objects.get(id=data["category"]).id
                except Category.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    data["category"] = Category.objects.get(name__iexact=data["category"]).id
                except Category.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerilizersPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def put(self, request):
        data = request.data
        if "id" not in data:
            return Response(data={"message": "id is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=data["id"])
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerilizersPOST(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        if "id" not in data:
            return Response(data={"message": "id is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=data["id"])
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerilizersPOST(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        if "id" not in data:
            return Response(data={"message": "id is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=data["id"])
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

