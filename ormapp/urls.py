# employees/urls.py
from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
    path('employees-list-create/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees-destroy/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update'
                                                                                          '-destroy'),
]
