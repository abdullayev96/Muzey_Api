from django.urls import path
from .views import *

urlpatterns = [
          path('', NewAPI.as_view()),
          path("<int:pk>/", NewsDetailAPI.as_view())


]