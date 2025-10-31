from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200, help_text="ФИО или название компании")
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name


class Order(models.Model):
    class Status(models.TextChoices):
        NEW = "NEW", "Новый"
        IN_PROGRESS = "INP", "В работе"
        DONE = "DON", "Сдан"
        CANCELED = "CAN", "Отменён"

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.NEW)
    due_date = models.DateField(null=True, blank=True, verbose_name="Дедлайн")
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.title} ({self.get_status_display()})"