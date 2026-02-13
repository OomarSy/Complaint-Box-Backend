from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from ..filters import ComplaintFilter
from ..tables import ComplaintTable
from ..forms import ComplaintForm
from ..models import Complaint


from apps.core.views.pages_views import BaseCRUDView, BaseDeleteView, BaseListView


class ListComplaint(BaseListView):
    model = Complaint
    table_class = ComplaintTable
    filterset_class = ComplaintFilter
    view_name = "Complaint"
    add_url_name = 'complaint-box:complaint_create'
    segment = "complaint"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-updated_at')

class DetailsComplaint(BaseCRUDView, DetailView):
    model = Complaint
    form_class = ComplaintForm
    view_name = "Employee complaint-box Details"
    details = True
    segment = "complaint"
    

class CreateComplaint(BaseCRUDView, CreateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'generic/form.html'
    create = True
    success_url = reverse_lazy('complaint-box:complaint_list')
    view_name = "Create Overtime"
    segment = "complaint"


class UpdateComplaint(BaseCRUDView, UpdateView):
    model = Complaint
    form_class = ComplaintForm
    success_url = reverse_lazy('complaint-box:complaint_list')
    view_name = "Update Overtime"
    segment = "complaint"


class DeleteComplaint(BaseDeleteView):
    model = Complaint
    view_name = "Delete Overtime"
    segment = "complaint"

@login_required
def complaint_box(request):
    # Get the current user
    user = request.user
    return render(request, 'pages/complaint/compliant-box.html', context={'user': user})
