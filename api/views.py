from django.shortcuts import render
from rest_framework.views import APIView
from api.serializers import UrlManageSerializer
from rest_framework.response import Response
from rest_framework import status
import string
import random

# Create your views here.

class ShortURL(APIView):
    def post(self, request):
        # serializer = UrlManageSerializer(data=request.data)
        # if serializer.is_valid():
        print(request.data)

        letters = string.ascii_letters
        key = ''.join(random.choice(letters) for i in range(7))

        serializer = UrlManageSerializer(data={'url':request.data['url'], 'short_url': key})

        # print(request.scheme+"://"+request.META['HTTP_HOST']+'/')

        if serializer.is_valid():
            serializer.save()
            return Response({'short_url': request.scheme+"://"+request.META['HTTP_HOST']+'/'+key}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

# class OriginalURL(APIView):
#     def get(self, request):
#         pass