from django.urls import path
from .api import CustomUserRegistration, CustomUserLogin, CustomUserLogout

urlpatterns = [
    path('register/', CustomUserRegistration.as_view(), name='register'),
    path('login/', CustomUserLogin.as_view(), name='login'),
    path('logout/', CustomUserLogout.as_view(), name='logout'),
]