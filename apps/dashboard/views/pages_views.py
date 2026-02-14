from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import user_passes_test
from apps.complaint_box.models import Complaint

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@superuser_required
def dashboard(request):
    today = timezone.now()
    last_7_days = today - timedelta(days=7)

    total_complaints = Complaint.objects.count()
    new_complaints = Complaint.objects.filter(status="new").count()
    in_progress = Complaint.objects.filter(status="in_progress").count()
    resolved = Complaint.objects.filter(status="resolved").count()
    rejected = Complaint.objects.filter(status="rejected").count()

    complaints_last_7_days = Complaint.objects.filter(
        created_at__gte=last_7_days
    ).count()

    complaints_by_reason = (
        Complaint.objects
        .values("reason")
        .annotate(count=Count("id"))
        .order_by("-count")
    )

    resolution_rate = 0
    if total_complaints > 0:
        resolution_rate = round((resolved / total_complaints) * 100, 1)

    context = {
        "total_complaints": total_complaints,
        "new_complaints": new_complaints,
        "in_progress": in_progress,
        "resolved": resolved,
        "rejected": rejected,
        "complaints_last_7_days": complaints_last_7_days,
        "complaints_by_reason": complaints_by_reason,
        "resolution_rate": resolution_rate,
    }

    return render(request, "pages/dashboard/dashboard.html", context)
