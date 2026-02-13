from django.urls import path

from ..views import apis_views

app_name = "users-api-v1"

urlpatterns = [
    
    path('complaints/', apis_views.ComplaintCreateAPIView.as_view(), name='complaint_create_api_v1'),

]
