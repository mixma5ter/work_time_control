# Generated by Django 4.2.18 on 2025-01-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bitrix_id',
            field=models.IntegerField(blank=True, help_text='Введите Битрикс ID сотрудника', null=True, verbose_name='Битрикс ID сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='card_number',
            field=models.CharField(help_text='Введите номер карты сотрудника', max_length=20, unique=True, verbose_name='Номер карты сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_name',
            field=models.CharField(help_text='Введите ФИО сотрудника', max_length=100, verbose_name='ФИО сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_checkin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время чекина'),
        ),
    ]
