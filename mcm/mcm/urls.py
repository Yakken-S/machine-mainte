from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView   # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mc_report.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
