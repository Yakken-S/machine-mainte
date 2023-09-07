from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class L1_Name(models.Model):
    l1_name = models.CharField(max_length=10, unique=True)
    machine_name = models.CharField(max_length=20)
    machine_type = models.CharField(max_length=10)
    machine_image  = models.FileField(blank=True)
    created_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="created_id_l1_name", to_field="id")
    updated_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="updated_id_l1_name", to_field="id")
    status_types = (
        ('01','正常'),
        ('02','修理中/稼働可能') ,
        ('03','修理中/稼働不可')
    )
    machine_status = models.CharField(max_length=20, choices=status_types, blank=True)
    def __str__(self):
        return f"{self.l1_name} - {self.machine_name}"

class Issue_History(models.Model):
    l1_name = models.ForeignKey('L1_Name', on_delete=models.CASCADE, related_name="l1_name_issue")
    alarm_num = models.ForeignKey('Alarm', on_delete=models.CASCADE, related_name="alarm_nums_issue")
    issue_types = (
        ('01','機械不具合'),
        ('02','電気不具合'),
        ('03','システム不具合'),
        ('04','加工精度不良')
    )
    issue_type = models.CharField(max_length=20, choices=issue_types, blank=True)
    issue_title = models.TextField()
    issue_detail = models.TextField()
    issue_treatment = models.TextField()
    issue_freeinput = models.TextField()
    issue_datetime = models.DateTimeField(auto_now=True)
    issue_fixparts = models.CharField(max_length=20)
    issue_fixdate = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    created_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="created_l1_name_issue", to_field="id")
    updated_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="updated_l1_name_issue", to_field="id")
    file_quotation = models.FileField(blank=True)
    file_report  = models.FileField(blank=True)
    file_image1  = models.FileField(blank=True)
    file_image2  = models.FileField(blank=True)
    
    def __str__(self):
        return f"{self.l1_name} - {self.alarm_num} - {self.issue_title}"

class Alarm(models.Model):
    alarm_num = models.CharField(max_length=10)
    alarm_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.alarm_num} - {self.alarm_name}"