from django.db import models


class Complaint(models.Model):

    class ComplaintStatus(models.TextChoices):
        NEW = 'new', 'جديدة'
        IN_PROGRESS = 'in_progress', 'قيد المعالجة'
        RESOLVED = 'resolved', 'تم الحل'
        REJECTED = 'rejected', 'مرفوضة'

    class ComplaintReason(models.TextChoices):
        WORK_ENVIRONMENT = 'work_environment', 'بيئة العمل'
        MANAGEMENT = 'management', 'الإدارة'
        SALARY = 'salary', 'الراتب'
        HARASSMENT = 'harassment', 'تحرش / إساءة'
        OTHER = 'other', 'أخرى'

    title = models.CharField(
        max_length=255
    )

    reason = models.CharField(
        max_length=50,
        choices=ComplaintReason.choices
    )

    custom_reason = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="يجب ملؤه إذا كان السبب 'أخرى'"
    )
    
    description = models.TextField()

    extra_data = models.JSONField(
        blank=True,
        null=True,
        help_text="معلومات غير تعريفية مثل القسم أو الفرع"
    )

    status = models.CharField(
        max_length=20,
        choices=ComplaintStatus.choices,
        default=ComplaintStatus.NEW
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title
