import django_filters
from django.db.models import Q
from .models import Complaint
from apps.core.filters import BaseFilterSet


class ComplaintFilter(BaseFilterSet):

    # فلترة بنطاق تاريخ الإنشاء
    created_at = django_filters.DateTimeFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'type': 'datetime-local'}
        )
    )

    # بحث نصي احترافي
    search = django_filters.CharFilter(
        method="filter_search",
        label="بحث"
    )

    # فلترة الشكاوى التي تحتوي custom_reason فقط
    has_custom_reason = django_filters.BooleanFilter(
        method="filter_has_custom_reason",
        label="يحتوي سبب مخصص"
    )

    # ترتيب النتائج
    ordering = django_filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('status', 'status'),
        ),
        field_labels={
            'created_at': 'تاريخ الإنشاء',
            'status': 'الحالة',
        }
    )

    class Meta:
        model = Complaint
        fields = [
            'status',
            'reason',
            'created_at',
        ]

    # =============================
    # Custom Filters
    # =============================

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value) |
            Q(custom_reason__icontains=value)
        )

    def filter_has_custom_reason(self, queryset, name, value):
        if value:
            return queryset.exclude(custom_reason__isnull=True).exclude(custom_reason='')
        return queryset
