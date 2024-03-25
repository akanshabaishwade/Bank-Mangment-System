from django.contrib import admin
from .models import Account, Transaction, Loan, Investment, DepositSlip, WithdrawalSlip, LoanPayment

class AccountAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customuser_email', 'balance', 'interest_rate', 'minimum_balance', 'opening_date', 'closed', 'bank_name', 'branch_name', 'account_type', 'created_by', 'updated_by', 'created_at', 'updated_at')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'amount', 'date', 'description', 'reference_number', 'created_by', 'updated_by', 'created_at', 'updated_at')

class LoanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'loan_type', 'amount', 'interest_rate', 'term_months', 'status', 'created_by', 'updated_by', 'created_at', 'updated_at')

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'investment_type', 'amount', 'maturity_date', 'expected_return', 'created_by', 'updated_by', 'created_at', 'updated_at')

class DepositSlipAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'date', 'employee', 'created_by', 'updated_by', 'updated_at')

class WithdrawalSlipAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'date', 'employee', 'created_by', 'updated_by', 'updated_at')

class LoanPaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'amount', 'payment_date', 'created_by', 'updated_by', 'updated_at')

# Register your models with the custom admin classes
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Investment, InvestmentAdmin)
admin.site.register(DepositSlip, DepositSlipAdmin)
admin.site.register(WithdrawalSlip, WithdrawalSlipAdmin)
admin.site.register(LoanPayment, LoanPaymentAdmin)
