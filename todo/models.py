from django.db import models
from django.utils import timezone

STATUS = (
    ('Pending','Pending'),
    ('Done','Done')
)


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS,max_length=20,default='Pending')
    