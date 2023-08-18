from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

class L1_Name(models.Model):
    l1_name = models.CharField(max_length=10, unique=True)
    machine_name = models.CharField(max_length=20)
    machine_type = models.CharField(max_length=10)
    created_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="created_id_l1_name")
    updated_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="updated_id_l1_name")

    def __str__(self):
        return self.l1_name,self.machine_name

class Issue_History(models.Model):
    l1_name = models.ForeignKey('L1_Name', on_delete=models.CASCADE, related_name="l1_name_issue")
    alarm_num = models.ForeignKey('Alarm', on_delete=models.CASCADE, related_name="alarm_nums_issue")
    issue_types = (
        ('01','機械不具合'),
        ('02','電気不具合'),
        ('03','システム不具合'),
        ('04','加工精度不良'),
    )
    issue_type = models.CharField(max_length=20, choices=issue_types, blank=True)
    issue_title = models.TextField()
    issue_detail = models.TextField()
    issue_treatment = models.TextField()
    issue_freeinput = models.TextField()
    issue_datetime = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    created_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="created_l1_name_issue")
    updated_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="updated_l1_name_issue")
    file_quotation = models.FileField()
    file_report  = models.FileField()
    file_image1  = models.FileField()
    file_image2  = models.FileField()
    
    def __str__(self):
        return f"{self.l1_name} - {self.alarm_num} - {self.issue_title}"

class Alarm(models.Model):
    alarm_num = models.CharField(max_length=10)
    alarm_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.alarm_num} - {self.alarm_name}"