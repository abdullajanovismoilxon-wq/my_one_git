from django.urls import path
from .views import index, register, registered
urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('registered/', registered, name='registered'),
]