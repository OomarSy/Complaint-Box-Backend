from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Complaint

from apps.core.mixins import ActiveNormalUserFormMixin
from apps.core.forms import BaseModelForm


class ComplaintForm(ActiveNormalUserFormMixin, BaseModelForm):
    SUBMIT_TEXT = _('Save Complaint')

    class Meta(BaseModelForm.Meta):
        model = Complaint
        fields = '__all__'
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        hidden_in_create_fields=['hours']