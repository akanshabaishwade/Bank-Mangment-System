from django.shortcuts import render
from Employee.models import *
from django.db import models
from User.models import *
# Create your views here.


class Account(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customuser_email = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="accounts",
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
        related_name="accounts_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="accounts_updated_by",
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
        related_name="transactions_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="transactions_updated_by",
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
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="loans_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="loans_updated_by",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)


class Investment(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    investment_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    maturity_date = models.DateField(blank=True, null=True)
    expected_return = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="investments_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="investments_updated_by",
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
        related_name="deposit_slips_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="deposit_slips_updated_by",
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
        related_name="withdrawal_slips_created_by",
        on_delete=models.CASCADE,
    )
    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="withdrawal_slips_updated_by",
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
        related_name="loan_payments_created_by",
        on_delete=models.CASCADE,
    )

    updated_by = models.ForeignKey(
        CustomUser,
        to_field="email",
        related_name="loan_payments_updated_by",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)

