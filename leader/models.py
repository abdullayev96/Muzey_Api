from django.db import models
from baseapp.models import  BaseModel



class Leader(BaseModel):
     name = models.CharField(max_length=300, verbose_name="Rahbar ismi")
     about = models.CharField(max_length=100, verbose_name="Lavozimi")
     number = models.CharField(max_length=20, verbose_name="Tel nomeri:")
     image = models.ImageField(upload_to="note/", verbose_name="Rasm joyi")
     email  = models.EmailField(unique=True,)


     def __str__(self):
          return self.name



     class Meta:
          verbose_name= "Rahbar"



