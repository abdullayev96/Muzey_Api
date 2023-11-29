from django.urls import path
from .views import LeaderAPI



urlpatterns = [
          path('', LeaderAPI.as_view())
]