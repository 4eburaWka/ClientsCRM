from django.db import models

class Customer(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    name = models.CharField(verbose_name="ФИО или название компании", max_length=200, help_text="ФИО или название компании")
    phone = models.CharField(verbose_name="телефон", max_length=50, blank=True)
    email = models.EmailField(verbose_name="почта", blank=True)
    note = models.TextField(verbose_name="заметки", blank=True)

    created_at = models.DateTimeField(verbose_name="дата и время начала сотрудничества", auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    class Status(models.TextChoices):
        NEW = "NEW", "Новый"
        IN_PROGRESS = "INP", "В работе"
        DONE = "DON", "Сдан"
        CANCELED = "CAN", "Отменён"

    customer = models.ForeignKey(Customer, verbose_name="клиент", on_delete=models.CASCADE, related_name="orders")
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField( blank=True, verbose_name="Описание")
    status = models.CharField(verbose_name="статус", max_length=3, choices=Status.choices, default=Status.NEW)
    due_date = models.DateField( null=True, blank=True, verbose_name="Дедлайн")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Сумма, ₽")
    created_at = models.DateTimeField(verbose_name="дата начала разработки", auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
