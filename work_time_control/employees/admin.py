import logging
import os

import requests
from django.contrib import admin
from dotenv import load_dotenv

from .models import Employee

logger = logging.getLogger('work_time_control')

load_dotenv()
WEB_HOOK = os.getenv('WEB_HOOK')


@admin.action(description='Обновить данные из Битрикс24')
def update_from_bitrix24(modeladmin, request, queryset):
    try:
        bitrix24_url = WEB_HOOK + 'user.get.json'
        logger.info(f"Bitrix24 URL: {bitrix24_url}")

        response = requests.get(bitrix24_url)
        response.raise_for_status()
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Raw response content: {response.content}")
        users = response.json()['result']

        filtered_users = [user for user in users if 'UF_USR_1739295687230' in user]

        for user in filtered_users:
            logger.info(f"Processing user data: {user}")
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
                logger.info("Employee created/updated successfully")
                print(f"Создан сотрудник: {employee_name}")
            else:
                logger.exception("Error creating/updating employee")
                print(f"Обновлен сотрудник: {employee_name}")

    except requests.exceptions.RequestException as e:
        # Обработка ошибок запроса
        logger.exception(f"Error communicating with Bitrix24: {e}")
        print(f"Ошибка запроса к Битрикс24: {e}")
    except Exception as e:
        # Обработка других ошибок
        logger.exception(f"An unexpected error occurred: {e}")
        print(f"Ошибка: {e}")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('bitrix_id', 'card_number', 'employee_name', 'last_checkin', 'is_active')
    list_display_links = ('employee_name',)
    list_filter = ('is_active',)
    search_fields = ('card_number', 'employee_name')
    actions = [update_from_bitrix24]
