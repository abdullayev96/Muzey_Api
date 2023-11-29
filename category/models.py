from django.db import models
from baseapp.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=200, verbose_name="Kateriya nomi:")

    def __str__(self):
       return self.name

    class Meta:
         verbose_name =  "Kategoriya_"



class Exhibit(BaseModel):
     name = models.CharField(max_length=300, verbose_name="Eksponat nomi:")
     year = models.CharField(max_length=40, verbose_name="Eksponat yaratilgan yil:")
     task = models.CharField(max_length=300, verbose_name="Eksponat Vazifasi:")
     image = models.ImageField(upload_to="img/", verbose_name="Rasm joyi:")
     body = models.TextField(verbose_name="Eksponatlar haqida:")
     file = models.FileField(verbose_name="Audio fayl:")
     image_one = models.ImageField(upload_to='image/', blank=False)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")

     def __str__(self):
         return self.name

     class Meta:
          verbose_name = "Eksponat_"


