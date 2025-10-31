from datetime import timedelta
from django.db.models import Count
from django.shortcuts import render
from django.utils.timezone import now

from .models import Order


def dashboard(request):
    """
    Дашборд: фильтрация по приближающимся дедлайнам.
    Параметр ?days=N (3/7/14/30) — показывает все заказы с дедлайном <= today+N,
    исключая «Сдан».
    Также выводит агрегаты по статусам.
    """
    # --- фильтр дней ---
    try:
        days = int(request.GET.get("days", 7))
    except ValueError:
        days = 7
    if days not in (3, 7, 14, 30):
        days = 7

    today = now().date()
    limit_date = today + timedelta(days=days)

    # список «приближающихся» заказов
    upcoming = (
        Order.objects
        .exclude(status=Order.Status.DONE)
        .exclude(due_date=None)
        .filter(due_date__lte=limit_date)
        .order_by("due_date", "title")
    )

    # агрегаты по статусам
    raw_stats = (
        Order.objects
        .values("status")
        .annotate(cnt=Count("id"))
        .order_by()
    )
    status_titles = dict(Order.Status.choices)
    stats = [
        {"code": row["status"], "title": status_titles.get(row["status"], row["status"]), "count": row["cnt"]}
        for row in raw_stats
    ]

    # отдельно просроченные (due_date < today, не «Сдан»)
    overdue = (
        Order.objects
        .exclude(status=Order.Status.DONE)
        .exclude(due_date=None)
        .filter(due_date__lt=today)
        .order_by("due_date")
    )

    context = {
        "today": today,
        "days": days,
        "upcoming": upcoming,
        "stats": stats,
        "overdue": overdue,
        "status_titles": status_titles,
    }
    return render(request, "dashboard.html", context)


def orders_public(request):
    """
    Публичный read-only список заказов (без отменённых).
    Убрали финансовые поля; оставили фокус на статусе и сроках.
    """
    orders = (
        Order.objects
        .exclude(status=Order.Status.CANCELED)
        .order_by("-created_at")[:200]
    )
    return render(request, "orders_public.html", {"orders": orders})