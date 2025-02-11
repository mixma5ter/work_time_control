# Generated by Django 4.2.18 on 2025-01-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_bitrix_id_alter_employee_card_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('employee_name',), 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.UniqueConstraint(fields=('bitrix_id', 'card_number'), name='unique_contest_model'),
        ),
    ]
