from django.urls import path
from .views import *


urlpatterns = [
          path('', AboutAPI.as_view()),
          path('job/',LeaderAPI.as_view()),
          path('structure/', StructureAPI.as_view())


]

