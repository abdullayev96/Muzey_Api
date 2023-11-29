from django.db import models
from baseapp.models import  BaseModel


contact =[
          (1, "Viktorinali"),(2, "Oddiy"),
          (3, "Mobile Ilovali")
]

NEW = "o'zbekcha"
REJECTED = "english"
Sion = "ruscha"



STATUS_CHOICES = (
(NEW, 'uz'),
(REJECTED, 'en'),
(Sion, 'ru')

)


class Contact(BaseModel):
      f_name = models.CharField(max_length=100, verbose_name="Ismi*")
      l_name = models.CharField(max_length=100, verbose_name="Familiyasi*")
      email = models.EmailField(unique=True, verbose_name="Email nomi*")
      phone = models.CharField(max_length=20, verbose_name="Boglanish telefoni*")
      day_time = models.CharField(max_length=20, verbose_name="Tashrif kuni va soati*")
      num_people = models.CharField(max_length=20, verbose_name="Tashrifchila soni*")
      obj_name = models.CharField(max_length=20, verbose_name="Muassa nomi*")
      type_excursion   =  models.IntegerField(choices=contact, default=1, verbose_name="ekskursiya turi*")
      language_excursion = models.CharField(max_length=9, choices=STATUS_CHOICES,
                                            default="uz", verbose_name="ekskursiya tili*")



      def __str__(self):
        return self.f_name


      class Meta:
          verbose_name= "Boglanish"