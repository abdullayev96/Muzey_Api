from django.shortcuts import render
from .serializers import *
from .models import Category, Exhibit
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from  django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework import filters
from rest_framework.generics import ListAPIView



# class FooFilter(DjangoFilterBackend):
#
#     def filter_queryset(self, request, queryset, view):
#         filter_class = self.get_filter_class(view, queryset)
#
#         if filter_class:
#             return filter_class(request.query_params, queryset=queryset, request=request).qs
#         return queryset
#
# class ExhibitAPI(APIView):
#
#     filter_fields = ('cat', )
#
#     def get(self, request, format=None):
#         queryset = Exhibit.objects.all()
#
#         f = FooFilter()
#         filtered_queryset = f.filter_queryset(request, queryset, self)
#
#         if filtered_queryset.exists():
#             serializer = ExhibitSerializer(queryset, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response([], status=status.HTTP_200_OK)



class ExhibitAPI(ListAPIView):
      queryset = Exhibit.objects.all()
      serializer_class = ExhibitSerializer

      # def get(self, request):
      #     try:
      #        data = request.data
      #        all = Exhibit.objects.all()
      #        serializers = ExhibitSerializer(all, many=True, context={'request': self.request})
      #        return Response({"data":serializers.data})
      #
      #     except Exception as e:
      #          print(e)
      #
      #
      #     return Response({"status":status.HTTP_400_BAD_REQUEST})


      filter_backends = [DjangoFilterBackend]
      filterset_fields = ['category']



class DetailExhibitAPI(APIView):
     def get(self, request, pk):
         try:
              one = Exhibit.objects.get(id=pk)
              serializer = DetailExhibitSerializer(one, context={'request': self.request})
              return Response({"data":serializer.data})

         except Exception as e:
               print(e)


         return Response({"status":status.HTTP_400_BAD_REQUEST})