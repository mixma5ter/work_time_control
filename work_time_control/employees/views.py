import locale

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
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
    locale.setlocale(locale.LC_TIME, 'ru_RU')

    # Обработка AJAX запросов
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            last_employee = Employee.objects.latest('last_checkin')
            formatted_last_checkin = timezone.localtime(last_employee.last_checkin).strftime("%d %B %Y г., %H:%M:%S")

            data = {
                'card_number': last_employee.card_number,
                'employee_name': last_employee.employee_name,
                'last_checkin': formatted_last_checkin,
                'is_active': last_employee.is_active,
            }
            return JsonResponse(data)
        except Employee.DoesNotExist:
            return JsonResponse({'message': 'No checkins yet'})

    # Обработка обычных запросов (не AJAX)
    else:
        try:
            last_employee = Employee.objects.latest('last_checkin')
            formatted_last_checkin = timezone.localtime(last_employee.last_checkin).strftime("%d %B %Y г., %H:%M")

            context = {
                'card_number': last_employee.card_number,
                'employee_name': last_employee.employee_name,
                'last_checkin': formatted_last_checkin,
                'is_active': last_employee.is_active,
            }
        except Employee.DoesNotExist:
            context = {'message': 'No checkins yet'}
        return render(request, 'employees/index.html', context)
