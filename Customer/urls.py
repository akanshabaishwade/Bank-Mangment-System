from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import api

router = DefaultRouter()
router.register(r'accounts', api.AccountViewSet)
router.register(r'transactions', api.TransactionViewSet)
router.register(r'loans', api.LoanViewSet)
router.register(r'investments', api.InvestmentViewSet)
router.register(r'deposit_slips', api.DepositSlipViewSet)
router.register(r'withdrawal_slips', api.WithdrawalSlipViewSet)
router.register(r'loan_payments', api.LoanPaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
