from django.shortcuts import render
from ormapp.models import Employee
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ormapp.serializers import EmployeeSerializer, CustomPageNumberPagination
from rest_framework import generics
from rest_framework.generics import ListAPIView


def get_all_employees(request=None):
    # Number of employees to display per page
    items_per_page = 10

    # Get all employees
    all_employees = Employee.objects.all()

    # Create a Paginator object
    paginator = Paginator(all_employees, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        employees_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        employees_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page.
        employees_page = paginator.page(paginator.num_pages)

    return render(request, 'employee_list.html', {'employees_page': employees_page})


def get_employee_with_state(request):
    state_param = request.GET.get('state', None)
    if not state_param:
        # If state parameter is not provided, you may handle this case accordingly
        return render(request, 'error.html', {'message': 'State parameter is required'})

    employees = Employee.objects.filter(state=state_param)

    if not employees:
        return render(request, 'no_results.html', {'state_param': state_param})

    return render(request, 'emp.html', {'employees': employees, 'state_param': state_param})


# ----------------REST FRAMEWORK STARTS-----------------------------------------------------------------------


# class EmployeeListCreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

class EmployeeListCreateView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPageNumberPagination


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
