from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from datetime import timedelta

from apps.users.models import User

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@superuser_required
def dashboard(request):
    # Get the current user
    user = request.user
    return render(request, 'pages/dashboard/dashboard.html', context={'user': user})
