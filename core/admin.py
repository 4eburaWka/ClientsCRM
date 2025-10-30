from django.contrib import admin
from .models import Customer, Order

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    fields = ("title", "status", "due_date", "amount")

@admin.action(description="Отметить выбранные заказы как Сдан")
def make_done(modeladmin, request, queryset):
    queryset.update(status=Order.Status.DONE)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at")
    search_fields = ("name", "email", "phone")
    inlines = [OrderInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("title", "customer", "status", "due_date", "amount", "created_at")
    list_filter = ("status", "due_date", "created_at")
    search_fields = ("title", "customer__name")
    actions = [make_done]
