from rest_framework.views import APIView, Response
from rest_framework import status
from .models import *
from .serializers import *



def get_client_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
          ip = address.split(',')[0]
    else:
          ip = request.META.get('REMOTE_ADDR')

    return ip


class NewAPI(APIView):
     def get(self, request):
          ip = get_client_ip(self.request)

          if IpModel.objects.filter(ip=ip).exists():
               new = News.objects.all()
               new.views.add(IpModel.objects.get(ip=ip))

          else:
              IpModel.objects.create(ip=ip)
              #new_id = request.GET.get('pk')
              new = News.objects.all()
              new.views.add(IpModel.objects.get(ip=ip))
          serializers = NewSerializer(new, context={'request': self.request})

          return Response(serializers.data)

          # def get(self, request):
          #          try:
          #             new = News.objects.all()
          #             serializers   = NewSerializer(new, many=True, context={'request': self.request})
          #             return Response({"data":serializers.data})
          #
          #          except Exception as e:
          #               print(e)
          #
          #          return Response({"status":status.HTTP_400_BAD_REQUEST})


class NewsDetailAPI(APIView):

          # def get(self, request, pk=None):
          #     if pk:
          #        user = News.objects.get(id=pk)
          #        serializer = NewsDetailSerializers(user, context={'request': self.request})
          #        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
          #
          #     user = News.objects.all()
          #     serializer = NewsSerializer(user, many=True)
          #     return Response({"data": serializer.data}, status=status.HTTP_200_OK)

     def get(self, request, pk):
          ip = get_client_ip(self.request)

          if IpModel.objects.filter(ip=ip).exists():
              new_id = pk
              new = News.objects.get(pk=new_id)
              new.views.add(IpModel.objects.get(ip=ip))

          else:
              IpModel.objects.create(ip=ip)
              new_id = request.GET.get('pk')
              new = News.objects.get(pk=new_id)
              new.views.add(IpModel.objects.get(ip=ip))
          serializers = NewDetailSerializer(new, context={'request': self.request})

          return Response(serializers.data)
