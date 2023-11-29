from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
      class Meta:
          model = Img
          fields  = ['image']




class AboutSerializer(serializers.ModelSerializer):
      images = ImageSerializer(many=True, read_only=True)

      class Meta:
          model = About
          fields = ['id', 'name', 'images',  'body','image']



class JobSerializer(serializers.ModelSerializer):
      class Meta:
          model = Leader
          fields = ['id','image','job', 'full_name', 'phone','email']


class StructureSerializer(serializers.ModelSerializer):
      class Meta:
          model = Structure
          fields = ['image']


