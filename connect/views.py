from django.shortcuts import render
from .models import Contact
from rest_framework import status
from .serializers import ContactSerializer
from rest_framework.views import APIView, Response
from rest_framework.generics import ListCreateAPIView

#
# class ContactAPI(APIView):
#       def post(self, request):
#           try:
#               data = request.data
#               serializer = ContactSerializer(data=data)
#               if serializer.is_valid(raise_exception=True):
#                  serializer.save()
#                  return Response({"data":serializer.data})
#           except Exception as e:
#               print(e)
#
#           return Response({"status":status.HTTP_400_BAD_REQUEST})



class ContactAPI(ListCreateAPIView):
     queryset = Contact.objects.all()
     serializer_class = ContactSerializer