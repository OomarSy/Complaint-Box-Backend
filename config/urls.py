from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import include, path, re_path
from apps.users.views.pages_views import index

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    path('dashboard/', include(('apps.dashboard.urls.pages', 'dashboard'), namespace="dashboard")),
    
    path("admin/", admin.site.urls),
    
    path('', index, name="index"),
    
    path("", include('admin_volt.urls')),
    
    
    #Apps URLs
    path('users/', include(('apps.users.urls.pages', 'users'), namespace="users")),
    path('users/api/v1/', include(('apps.users.urls.api_v1', 'users-api-v1'), namespace="users-api-v1")),
    
    #media
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
