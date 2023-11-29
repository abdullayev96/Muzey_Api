from django.shortcuts import render
from rest_framework.generics import  ListAPIView
from rest_framework.views import  APIView, Response
from .models import Gallery
from rest_framework import status
from .serializers import *


class GalleryAPI(ListAPIView):
      queryset = Gallery.objects.all()
      serializer_class = GallerySerializer



class DetailGalleryAPI(APIView):
      def get(self, request, pk=None):
          try:
             obj = Gallery.objects.get(id=pk)
             serializers  = DetailGallerySerializer(obj, context={'request': self.request})
             return Response({"data":serializers.data})

          except Exception as e:
                print(e)

          return Response({"status":status.HTTP_400_BAD_REQUEST})

