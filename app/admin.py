from django.contrib import admin

from app.models import Client, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Client)
