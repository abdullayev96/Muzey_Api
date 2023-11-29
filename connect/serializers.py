from rest_framework import serializers
from .models import *



class ContactSerializer(serializers.ModelSerializer):
      class Meta:
          model = Contact
          fields = ['f_name', 'l_name', 'email', 'phone', 'day_time', 'num_people',
                    'obj_name', 'obj_name', 'type_excursion', 'language_excursion']