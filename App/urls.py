from django.urls import path
from App.views import index


urlpatterns = [
    path('', index, name="index"),
]
