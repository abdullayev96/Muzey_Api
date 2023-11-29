from  rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
      class Meta:
           model = Fotos
           fields  = ['images']




class NewSerializer(serializers.ModelSerializer):
     views = serializers.SerializerMethodField()

     class Meta:
          model  = News
          fields  = ['id','image_one', 'name', 'created_at', 'views']


     def get_views(self, obj):
         return obj.views.count()




class NewDetailSerializer(serializers.ModelSerializer):
      views = serializers.SerializerMethodField()
      image = ImageSerializer(many=True, read_only=True)


      class Meta:
          model  = News
          fields = ['name', 'created_at', 'views', 'image', 'body', 'f_link', 't_link']

      def get_views(self, obj):
          return obj.views.count()