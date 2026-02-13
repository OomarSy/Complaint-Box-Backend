from django.utils.translation import gettext_lazy as _
import django_tables2 as tables

from .models import Complaint
from apps.core.tables import BaseTable



class ComplaintTable(BaseTable):
    
    BUTTONS = {
        'view': {'label': _('View'), 'url_name': 'complaint-box:complaint_detail'},
        'edit': {'label': _('Edit'), 'url_name': 'complaint-box:complaint_update'},
        'delete': {'label': _('Delete'), 'url_name': 'complaint-box:complaint_delete'},
    }

    class Meta(BaseTable.Meta):
        model = Complaint
        fields = ('id','title', 'reason', 'status', 'created_at')
