from rest_framework import serializers
from .models import Img, Gallery


class ImgSerializer(serializers.ModelSerializer):
     class Meta:
          model = Img
          fields  =  ['image']




class GallerySerializer(serializers.ModelSerializer):


     class Meta:
          model = Gallery
          fields  = ['id', 'name', 'image_one']


class DetailGallerySerializer(serializers.ModelSerializer):
     images = ImgSerializer(many=True, read_only=True)

     class Meta:
          model = Gallery
          fields = ['images']
