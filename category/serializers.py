from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
     class Meta:
          model  = Category
          fields  = ['name']



class ExhibitSerializer(serializers.ModelSerializer):
     category = CategorySerializer()
     class Meta:
          model  = Exhibit
          fields  = ['id','category','image', 'name', 'body']



class DetailExhibitSerializer(serializers.ModelSerializer):
     class Meta:
          model = Exhibit
          fields  = ['year', 'name','task', 'file', 'image', 'body', 'image_one']