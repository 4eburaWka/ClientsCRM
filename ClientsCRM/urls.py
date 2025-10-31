from django.contrib import admin
from django.urls import path
from core.views import dashboard, orders_public

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard, name="dashboard"),
    path("orders/", orders_public, name="orders_public"),
]