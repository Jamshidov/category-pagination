from django.urls import path
from .views import *

app_name = 'capp2'

urlpatterns = [
    path('', home, name='home'),
]