from django.db import models
from baseapp.models import BaseModel



class Img(models.Model):
     image = models.ImageField(upload_to="note/", verbose_name="rasmlar")


     class Meta:
          verbose_name = "Rasm"


class Gallery(BaseModel):
      name = models.CharField(max_length=100, verbose_name="Galeriya nomi")
      image_one = models.ImageField(upload_to='new/', verbose_name="bitta rasm*")
      images = models.ManyToManyField(Img, verbose_name="toplami", related_name="images")

      def __str__(self):
          return self.name


      class Meta:
          verbose_name = "Galeriya"



