from django.urls import path
from .views import *



urlpatterns = [
          path('', GalleryAPI.as_view()),
          path('<int:pk>/', DetailGalleryAPI.as_view())

]