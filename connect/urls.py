from django.urls import path
from .views import *


urlpatterns = [
          path('', ContactAPI.as_view())

]