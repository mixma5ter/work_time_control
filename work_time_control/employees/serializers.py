from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # 'bitrix_id', 'card_number', 'employee_name', 'last_checkin', 'is_active'
