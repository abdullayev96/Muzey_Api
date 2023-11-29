from django.db import models
from baseapp.models import BaseModel



class Img(BaseModel):
      image  = models.ImageField(upload_to="rasm/")

      class Meta:
          verbose_name = "Rasm"



class About(BaseModel):
      name= models.CharField(max_length=300, verbose_name="Muzey nomi")
      body = models.TextField(verbose_name="Muzey haqida")
      image = models.ImageField(upload_to="note/", verbose_name="image")
      images  = models.ManyToManyField(Img, verbose_name="Rasmlar", related_name="images")


      def __str__(self):
          return self.name

      class Meta:
          verbose_name  = "Muzey haqida"



class Leader(BaseModel):
     job = models.CharField(max_length=200, verbose_name="Kasbi")
     full_name = models.CharField(max_length=300, verbose_name="Toliq rasm*")
     image = models.ImageField(upload_to="rote/", verbose_name="Rasmi*")
     phone = models.CharField(max_length=200, verbose_name="Telefon raqami*")
     email = models.EmailField(verbose_name="Email nomi*")

     def __str__(self):
          return self.full_name

     class Meta:
          verbose_name = "Muzey hodimlari*"


class Structure(models.Model):
      image = models.ImageField(upload_to='road/')


      class Meta:
          verbose_name = "Muzey tuzimlar"