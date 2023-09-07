from django.contrib import admin
from .models import L1_Name, Issue_History, Alarm, CustomUser

admin.site.register(L1_Name)
admin.site.register(Issue_History)
admin.site.register(Alarm)

