
# ------------------------------way 1---------------------------------

# from django.urls import path
# from . import api

# urlpatterns = [
#     # path('banks/', api.BankApi.as_view({'get': 'list'}), name='bank-list'),
#     # path('roles/', api.RoleApi.as_view(), name='role-list'),
#     # path('employees/', api.EmployeeApi.as_view(), name='employee-list'),
#     # path('salaries/', api.SalaryApi.as_view(), name='salary-list'),
# ]

# ------------------------------way 2----------------------------------

from rest_framework.routers import DefaultRouter
from . import api

# /banks/ (GET, POST)
# /banks/{id}/ (GET, PUT, PATCH, DELETE)

router = DefaultRouter()
router.register(r'banks', api.BankApi, basename='bank')
router.register(r'roles', api.RoleApi, basename='role')
router.register(r'employees', api.EmployeeApi, basename='employee')
router.register(r'salaries', api.SalaryApi, basename='salary')

urlpatterns = router.urls