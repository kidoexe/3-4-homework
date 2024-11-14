from django.urls import path
from .views import main, students

urlpatterns = [
    path('main/', main, name='main'),
    path('students/', students, name='students'),
]
