from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'card_number'
    # permission_classes = [permissions.IsAuthenticated]


def index(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            last_employee = Employee.objects.latest('last_checkin')
            data = {
                'name': last_employee.employee_name,
                'is_active': last_employee.is_active,
            }
            return JsonResponse(data)
        except Employee.DoesNotExist:
            return JsonResponse({'message': 'No checkins yet'})
    else:
        try:
            last_employee = Employee.objects.latest('last_checkin')
            context = {
                'name': last_employee.employee_name,
                'is_active': last_employee.is_active,
            }
        except Employee.DoesNotExist:
            context = {'message': 'No checkins yet'}
        return render(request, 'employees/index.html', context)
