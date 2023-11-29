from django.urls import path
from .views import *


urlpatterns = [
          path('', ExhibitAPI.as_view()),
          path('<int:pk>/', DetailExhibitAPI.as_view())
]