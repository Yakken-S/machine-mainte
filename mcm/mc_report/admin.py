from django.contrib import admin
from .models import User
from .models import L1_Name
from .models import Issue_History
from .models import Alarm

# Register your models here.

admin.site.register(User)
admin.site.register(L1_Name)
admin.site.register(Issue_History)
admin.site.register(Alarm)