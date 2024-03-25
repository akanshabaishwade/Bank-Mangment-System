from rest_framework import serializers
from .models import Account, Transaction, Loan, Investment, DepositSlip, WithdrawalSlip, LoanPayment

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'

class DepositSlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositSlip
        fields = '__all__'

class WithdrawalSlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithdrawalSlip
        fields = '__all__'

class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = '__all__'
