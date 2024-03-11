from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls')),
    path('customer', include('Customer.urls')),
    path('employee', include('Employee.urls')),
    path('services', include('Services.urls')),
    path('notifications', include('Notifications.urls')),


]
