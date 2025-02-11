import requests
from django.contrib import admin

from .models import Employee


@admin.action(description='Обновить данные из Битрикс24')
def update_from_bitrix24(modeladmin, request, queryset):
    try:
        bitrix24_url = 'https://mcko.bitrix24.ru/rest/262/eqfyx10uwv366c7e/user.get.json'

        response = requests.get(bitrix24_url)
        response.raise_for_status()
        users = response.json()['result']

        filtered_users = [user for user in users if 'UF_USR_1739295687230' in user]

        for user in filtered_users:
            bitrix_id = user.get('ID')
            card_number = user.get('UF_USR_1739295687230')
            employee_name = f"{user.get('LAST_NAME', '')} {user.get('NAME', '')} {user.get('SECOND_NAME', '')}".strip()

            obj, created = Employee.objects.update_or_create(
                bitrix_id=bitrix_id,
                defaults={
                    'card_number': card_number,
                    'employee_name': employee_name,
                }
            )

            if created:
                obj.is_active = False
                obj.save()
                print(f"Создан сотрудник: {employee_name}")
            else:
                print(f"Обновлен сотрудник: {employee_name}")

    except requests.exceptions.RequestException as e:
        # Обработка ошибок запроса
        print(f"Ошибка запроса к Битрикс24: {e}")
    except Exception as e:
        # Обработка других ошибок
        print(f"Ошибка: {e}")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('bitrix_id', 'card_number', 'employee_name', 'last_checkin', 'is_active')
    list_display_links = ('employee_name',)
    list_filter = ('is_active',)
    search_fields = ('card_number', 'employee_name')
    actions = [update_from_bitrix24]
