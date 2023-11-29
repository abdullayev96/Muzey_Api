from django.shortcuts import render
from rest_framework.generics import  ListAPIView
from .serializers import *
from .models import *


class ContactAPI(ListAPIView):
     queryset = Contact.objects.all()
     serializer_class = ContactsSerializer

