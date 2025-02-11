from django.db import models


class Employee(models.Model):
    """Модель сотрудника."""

    bitrix_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Битрикс ID сотрудника',
        help_text='Введите Битрикс ID сотрудника',
    )
    card_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Номер карты сотрудника',
        help_text='Введите номер карты сотрудника',
    )
    employee_name = models.CharField(
        max_length=100,
        verbose_name='ФИО сотрудника',
        help_text='Введите ФИО сотрудника',
    )
    last_checkin = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время чекина',
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Активность',
    )

    def __str__(self):
        return self.employee_name

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'
        ordering = ('employee_name',)
        constraints = [
            models.UniqueConstraint(
                fields=['bitrix_id', 'card_number'],
                name='unique_contest_model'
            )
        ]
