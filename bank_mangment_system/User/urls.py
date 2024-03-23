from django.urls import path
from .api import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('login/', LoginApi.as_view(), name='login'),
    path('logout/', logoutApi , name='logout'),

]