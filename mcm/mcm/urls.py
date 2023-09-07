from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mc_report.urls')),
    path("accounts/", include("allauth.urls")),
]
