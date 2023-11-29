from django_filters import rest_framework
from .models import *

class ExhibitFilter(rest_framework.FilterSet):
          #discount = rest_framework.BooleanFilter(method='get_discount')

      class Meta:
         model = Exhibit
         fields = ["category__name"]


          # def get_discount(self, queryset, name, value):
          #     return queryset.filter(discount__isnull=False)