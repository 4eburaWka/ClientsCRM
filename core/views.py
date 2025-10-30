from django.db.models import Count, Sum
from django.shortcuts import render
from django.utils.timezone import now
from .models import Order

def dashboard(request):
    stats = (
        Order.objects
        .values("status")
        .annotate(cnt=Count("id"))
        .order_by()
    )
    total_active = (
        Order.objects
        .exclude(status=Order.Status.DONE)
        .aggregate(s=Sum("amount"))["s"] or 0
    )
    upcoming = (
        Order.objects
        .exclude(status=Order.Status.DONE)
        .exclude(due_date=None)
        .order_by("due_date")[:5]
    )
    return render(request, "dashboard.html", {
        "stats": stats,
        "total_active": total_active,
        "upcoming": upcoming,
        "today": now().date(),
    })

def orders_public(request):
    orders = (
        Order.objects
        .exclude(status=Order.Status.CANCELED)
        .order_by("-created_at")[:50]
    )
    return render(request, "orders_public.html", {"orders": orders})
