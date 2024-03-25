from rest_framework import viewsets
from .models import Account, Transaction, Loan, Investment, DepositSlip, WithdrawalSlip, LoanPayment
from .serializers import AccountSerializer, TransactionSerializer, LoanSerializer, InvestmentSerializer, DepositSlipSerializer, WithdrawalSlipSerializer, LoanPaymentSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class DepositSlipViewSet(viewsets.ModelViewSet):
    queryset = DepositSlip.objects.all()
    serializer_class = DepositSlipSerializer

class WithdrawalSlipViewSet(viewsets.ModelViewSet):
    queryset = WithdrawalSlip.objects.all()
    serializer_class = WithdrawalSlipSerializer

class LoanPaymentViewSet(viewsets.ModelViewSet):
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer
