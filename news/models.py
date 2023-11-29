from django.db import models
from baseapp.models import BaseModel



class IpModel(models.Model):
    ip =  models.CharField(max_length=100)


    def __str__(self):
      return self.ip


class Fotos(BaseModel):
     images = models.ImageField(upload_to="img/", verbose_name="Rasm")

     class Meta:
         verbose_name = "Rasmla"




class News(BaseModel):
    name = models.CharField(max_length=200, verbose_name="Yangilik nomi:")
    body  = models.TextField(verbose_name="Rasm texti:")
    views  = models.ManyToManyField(IpModel, verbose_name="Korishlar soni", related_name="views", blank=True)
    image  = models.ManyToManyField(Fotos, verbose_name="Rasmlar:", related_name="image")
    image_one  = models.ImageField(upload_to="img/", verbose_name="Bitta rasm uchun:")
    f_link = models.URLField(max_length=4000, verbose_name="Facebook link *")
    t_link = models.URLField(max_length=4000, verbose_name="Telegram link *")



    def __str__(self):
        return self.name

    def total_views(self):
          return self.views.count()


    class Meta:
          verbose_name = "Yangilikla"

