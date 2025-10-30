import datetime

from django.db import models


class Project(models.Model):
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    client: "Client" = models.ForeignKey("Client", verbose_name="клиент", on_delete=models.SET_NULL, null=True)

    title: str = models.CharField(verbose_name="название", max_length=50)
    description: str = models.TextField(verbose_name="описание")
    total_cost: float = models.FloatField(verbose_name="итоговая стоимость разработки")

    start_work_date: datetime.date = models.DateField(verbose_name="начало разработки")
    stop_work_date: datetime.date = models.DateField(verbose_name="конец разработки", null=True)

    total_paid: float = models.FloatField(verbose_name="всего уплачено")

    def __str__(self):
        return self.title


class Client(models.Model):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    fullname: str = models.CharField(verbose_name="полное имя", max_length=50)
    start_partnership_date: datetime.datetime = models.DateTimeField(verbose_name="дата начала сотрудничества", auto_created=True)

    def __str__(self):
        return self.fullname
