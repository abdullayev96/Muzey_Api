from django.db import models
from baseapp.models import BaseModel



class Contact(BaseModel):
     address = models.CharField(max_length=200, verbose_name="Manzil:")
     phone  = models.CharField(max_length=300, verbose_name="Telefon:")
     bus =  models.CharField(max_length=100, verbose_name="Transport :")
     email = models.EmailField(verbose_name="E-mail:")
     image  = models.ImageField(upload_to="img/", verbose_name="Manzil rasmi:")

     class Meta:
          verbose_name = "Boglanish:"





