from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Account, Transaction, Loan, Investment, DepositSlip, WithdrawalSlip, LoanPayment
from datetime import date

User = get_user_model()

class AccountTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = User.objects.create_user(email='user@example.com', password='password')
        cls.account = Account.objects.create(
            customuser_email=cls.user,
            balance=1000,
            interest_rate=5,
            minimum_balance=500,
            opening_date=date.today(),
            closed=False,
            bank_name="Example Bank",
            branch_name="Example Branch",
            account_type="Checking",
            created_by=cls.user,
            updated_by=cls.user
        )

    def test_account_list(self):
        self.client.force_login(self.user)
        url = reverse('account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_detail(self):
        self.client.force_login(self.user)
        url = reverse('account-detail', kwargs={'pk': self.account.customer_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Repeat the structure for other models

class TransactionTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Assume user and account have been created
        cls.transaction = Transaction.objects.create(
            account=AccountTests.account,
            transaction_type='Deposit',
            amount=200,
            date=date.today(),
            description='Initial deposit',
            created_by=AccountTests.user,
            updated_by=AccountTests.user
        )

    def test_transaction_list(self):
        self.client.force_login(AccountTests.user)
        url = reverse('transaction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_transaction_detail(self):
        self.client.force_login(AccountTests.user)
        url = reverse('transaction-detail', kwargs={'pk': self.transaction.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

