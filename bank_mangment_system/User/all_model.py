from django.db import models
from User.models import *
from django_cryptography.fields import encrypt




class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_name = encrypt(models.CharField(max_length=255))
    branch = encrypt(models.CharField(max_length=255))
    address = encrypt(models.CharField(max_length=255, blank=True, null=True))
    established_date = encrypt(models.DateField(null=True, blank=True))

    def __str__(self):
        return f"{self.bank_name} - {self.branch}"


class Role(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    bank_name = models.ForeignKey(
        Bank,
        to_field="bank_id",
        related_name="bank_id_employee",
        on_delete=models.CASCADE,
    )
    employee_email = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Customer",
        on_delete=models.CASCADE,
    )
    branch = models.ForeignKey(Bank, on_delete=models.CASCADE)   
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    yearly_salary = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.employee_email.first_name} {self.employee_email.last_name} ({self.role})"  # Customize string representation



class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.amount} - {self.date}"
    






#------------------------------------------------------------------------------------------
    
from django.db import models
from User.models import *
from Employee.models import *
from django_cryptography.fields import encrypt

    
class Account(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customuser_email = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account",
        on_delete=models.CASCADE,
    )
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    minimum_balance = models.DecimalField(max_digits=10, decimal_places=2)
    opening_date = models.DateField()
    closed = models.BooleanField(default=False)
    bank_name = models.CharField(max_length=255, blank=True)
    branch_name = models.CharField(max_length=255, blank=True)
    account_type = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_updated_by",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)




    def __str__(self):
        return f"{self.customuser_email}'s Account"


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    reference_number = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_updated_by",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)




class Loan(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term_months = models.IntegerField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_updated_by",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)




class Investment(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    investment_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    maturity_date = models.DateField(blank=True, null=True)
    expected_return = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_updated_by",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)




class DepositSlip(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_updated_by",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)




class WithdrawalSlip(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_updated_by",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)




class LoanPayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="email_Account_updated_by",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)


# -----------------------------------------------------------------------------
    


class CustomUser(models.Model):
    customuser_id = models.AutoField(primary_key=True)
    username = encrypt(models.CharField(max_length=100))
    first_name = encrypt(models.CharField(max_length=150, blank=True))
    middle_name = encrypt(models.CharField(max_length=150, blank=True))
    last_name = encrypt(models.CharField(max_length=150, blank=True))
    email = encrypt(models.EmailField(unique=True))
    phone_number = encrypt(models.CharField(max_length=20, blank=True, null=True))
    date_of_birth = encrypt(models.DateField(blank=True, null=True))
    tax_id = encrypt(models.CharField(max_length=100, blank=True, null=True))
    address = encrypt(models.TextField(blank=True))
    country = encrypt(models.CharField(max_length=100, blank=True, null=True))
    password = encrypt(models.CharField(max_length=255))
    government_issued_id = encrypt(models.CharField(max_length=100, blank=True, null=True))
    customer_type = encrypt(models.CharField(max_length=100, blank=True, null=True))
    occupation = encrypt(models.CharField(max_length=100, blank=True, null=True))
    employer = encrypt(models.CharField(max_length=255, blank=True, null=True))
    communication_preferences = encrypt(models.CharField(max_length=255, blank=True, null=True))
    UserType = (("Customer", "Customer"), ("Employee", "Employee"))
    user_type = encrypt(models.CharField(max_length=256, choices=UserType))
    is_staff = encrypt(models.BooleanField(default=False))
    is_active = encrypt(models.BooleanField(default=True))
    date_joined = encrypt(models.DateTimeField(auto_now_add=True))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if hasattr(field, 'encrypt') and getattr(self, field.attname):
                setattr(self, field.attname, encrypt(getattr(self, field.attname).encode()))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

