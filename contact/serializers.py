from rest_framework import serializers
from .models import Contact



class  ContactsSerializer(serializers.ModelSerializer):
       class Meta:
          model = Contact
          fields  = ['address', 'phone', 'bus', 'email', 'image']