from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Leader
from .serializers import LeaderSerializer
from rest_framework.generics import ListAPIView




class LeaderAPI(APIView):
      def get(self, request):

          try:
              obj = Leader.objects.all()
              serializer = LeaderSerializer(obj, many=True, context={'request': self.request})

              return Response({'data':serializer.data})

          except Exception as e:
              print(e)

          return Response({"status": status.HTTP_404_NOT_FOUND})
