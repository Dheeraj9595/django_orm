from django.shortcuts import render
from ormapp.models import Employee


def get_all_employees(request=None):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def get_employee_with_state(request):
    state_param = request.GET.get('state', None)
    if not state_param:
        # If state parameter is not provided, you may handle this case accordingly
        return render(request, 'error.html', {'message': 'State parameter is required'})

    employees = Employee.objects.filter(state=state_param)

    if not employees:
        return render(request, 'no_results.html', {'state_param': state_param})

    return render(request, 'emp.html', {'employees': employees, 'state_param': state_param})

