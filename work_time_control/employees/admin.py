from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('bitrix_id', 'card_number', 'employee_name', 'last_checkin', 'is_active')
    list_display_links = ('employee_name',)
    list_filter = ('is_active',)
    search_fields = ('card_number', 'employee_name')
