
# Django imports
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),    # Incluimos core app urls
]
