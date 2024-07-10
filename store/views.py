# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Category
from store.serializers import CategorySerilizers


class CategoryAPI(APIView):
    def get(self, request):
        category = Category.objects.all()
        print(category)
        serializer = CategorySerilizers(category, many=True)
        return Response({"data":serializer.data})

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
