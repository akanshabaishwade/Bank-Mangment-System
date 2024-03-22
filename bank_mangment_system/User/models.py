from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
# from django_cryptography.fields import encrypt
# from encrypted_fields import EncryptedFieldMixin4
from cryptography.fernet import Fernet
import secrets  

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        for field_name in ['is_staff', 'is_superuser']:
            extra_fields.pop(field_name, None)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser):
#     customuser_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     middle_name = models.CharField(max_length=150, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20, blank=True)
#     UserType = (("Customer", "Customer"), ("Employee", "Employee"))
#     user_type = models.CharField(max_length=256, choices=UserType)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def __str__(self):
#         return self.email


from cryptography.fernet import Fernet
from django.db import models

# Generate a key for encryption
key = Fernet.generate_key()
encrypt = Fernet(key)

class CustomUser(models.Model):
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

    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is being created
            self.password = encrypt(self.password.encode())
            self.username = encrypt(self.username.encode())
            self.first_name = encrypt(self.first_name.encode())
            self.middle_name = encrypt(self.middle_name.encode())
            self.last_name = encrypt(self.last_name.encode())
            self.email = encrypt(self.email.encode())
            self.phone_number = encrypt(self.phone_number.encode()) if self.phone_number else None
            self.tax_id = encrypt(self.tax_id.encode()) if self.tax_id else None
            self.address = encrypt(self.address.encode()) if self.address else None
            self.country = encrypt(self.country.encode()) if self.country else None
            self.government_issued_id = encrypt(self.government_issued_id.encode()) if self.government_issued_id else None
            self.customer_type = encrypt(self.customer_type.encode()) if self.customer_type else None
            self.occupation = encrypt(self.occupation.encode()) if self.occupation else None
            self.employer = encrypt(self.employer.encode()) if self.employer else None
            self.communication_preferences = encrypt(self.communication_preferences.encode()) if self.communication_preferences else None
        super().save(*args, **kwargs)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True  # Change this based on your authentication logic


    def __str__(self):
        return self.email

