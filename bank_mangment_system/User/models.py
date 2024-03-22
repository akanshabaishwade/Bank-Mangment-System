from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    customuser_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    tax_id = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255)
    government_issued_id = models.CharField(max_length=100, blank=True, null=True)
    customer_type = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    employer = models.CharField(max_length=255, blank=True, null=True)
    communication_preferences = models.CharField(max_length=255, blank=True, null=True)
    UserType = (("Customer", "Customer"), ("Employee", "Employee"))
    user_type = models.CharField(max_length=256, choices=UserType)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

