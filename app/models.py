import datetime

from django.db import models


class Project(models.Model):
    client: "Client" = models.ForeignKey("Client", on_delete=models.SET_NULL, null=True)

    title: str = models.CharField(max_length=50)
    description: str = models.TextField()
    total_cost: float = models.FloatField()

    start_work_date: datetime.date = models.DateField()
    stop_work_date: datetime.date = models.DateField()

    total_paid: float = models.FloatField()


class Client(models.Model):
    fullname: str = models.CharField(max_length=50)
    start_partnership_date: datetime.datetime = models.DateTimeField(auto_now=True)
