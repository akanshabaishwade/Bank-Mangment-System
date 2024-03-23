from Employee.models import *
from django.db import models
from User.models import *
from django.db import models
from cryptography.fernet import Fernet

from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet



# Generate or load the key securely, using Django's SECRET_KEY
key = b'c9ZRtxBTyewCHI5lE92Mu-0LRpUHoPtVZt0LAaUOhsA='
cipher_suite = Fernet(key)


class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    established_date = models.DateField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="banks_created",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="banks_updated",
    )
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     # Encrypt the fields before saving
    #     self.bank_name_encrypted = cipher_suite.encrypt(self.bank_name.encode())
    #     self.branch_encrypted = cipher_suite.encrypt(self.branch.encode())
    #     if self.address:
    #         self.address_encrypted = cipher_suite.encrypt(self.address.encode())
    #     if self.established_date:
    #         self.established_date_encrypted = cipher_suite.encrypt(str(self.established_date).encode())
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.bank_name} - {self.branch}"


class Role(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="roles_created",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="roles_updated",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    bank = models.ForeignKey(
        Bank,
        to_field="bank_id",
        related_name="employees",
        on_delete=models.CASCADE,
    )
    employee_email = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="employee_emails",
        on_delete=models.CASCADE,
    )
    branch = models.ForeignKey(Bank, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    yearly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="employees_created",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="employees_updated",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_email.first_name} {self.employee_email.last_name} ({self.role})"

class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="salaries_created",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="salaries_updated",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee} - {self.amount} - {self.date}"
