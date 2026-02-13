from django.urls import path

from ..views import pages_views

app_name = "complaint_box"

urlpatterns = [
    
    path('', pages_views.complaint_box, name="complaint_box"),
    
    # Complaint Paths
    path('list', pages_views.ListComplaint.as_view(), name='complaint_list'),
    path('create/', pages_views.CreateComplaint.as_view(), name='complaint_create'),
    path('<int:pk>/', pages_views.DetailsComplaint.as_view(), name='complaint_detail'),
    path('<int:pk>/edit/', pages_views.UpdateComplaint.as_view(), name='complaint_update'),
    path('<int:pk>/delete/', pages_views.DeleteComplaint.as_view(), name='complaint_delete'),

]
