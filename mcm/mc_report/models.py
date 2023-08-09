from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    UserId = models.CharField(max_length=5)
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=10)

    def __str__(self):
        return self.UserName

class L1_Name(models.Model):
    L1_Name = models.CharField(max_length=10)
    MachineName = models.CharField(max_length=20)
    MachineType = models.CharField(max_length=10)
    CreatedId = models.CharField(max_length=5)
    UpdatedId = models.CharField(max_length=5)
    
    def __str__(self):
        return self.L1_Name,self.MachineName

class Issue_History(models.Model):
    L1_Name = models.CharField(max_length=10)
    AlarmNum = models.CharField(max_length=10)
    IssueType = models.TextField()
    IssueTitle = models.TextField()
    IssueDetail = models.TextField()
    IssueDatetime = models.DateTimeField(default=timezone.now)
    CreatedAt = models.DateTimeField(default=timezone.now)
    UpdatetedAt = models.DateTimeField(default=timezone.now)
    UserId = models.CharField(max_length=5)
    UpdatedId = models.CharField(max_length=5)
    File_Quotation = models.FileField()
    File_Report  = models.FileField()
    File_Image1  = models.FileField()
    File_Image2  = models.FileField()
        
    def __str__(self):
        return self.L1_Name, self.AlarmNum, self.IssueTitle


class Alarm(models.Model):
    AlarmNum = models.CharField(max_length=10)
    AlarmName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.AlarmNum, self.AlarmName