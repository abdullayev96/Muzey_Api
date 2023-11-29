from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import *
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import status
from .models import *


class AboutAPI(APIView):
     def get(self, request):
          try:
               about = About.objects.all()
               serializers = AboutSerializer(about, many=True, context={'request': self.request})
               return Response({"data":serializers.data})

          except Exception as e:
               print(e)

          return Response({"data":status.HTTP_400_BAD_REQUEST})




class LeaderAPI(APIView):
     def get(self, request):
          try:
               about = Leader.objects.all()
               serializers = JobSerializer(about, many=True, context={'request': self.request})
               return Response({"data":serializers.data})

          except Exception as e:
               print(e)

          return Response({"data":status.HTTP_400_BAD_REQUEST})


class StructureAPI(ListAPIView):
     queryset = Structure.objects.all()
     serializer_class = StructureSerializer