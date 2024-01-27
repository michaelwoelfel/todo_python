from django.db import models
from datetime import date,datetime
from django.conf import settings



# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    date = models.DateField(default=date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,default= None)
    
    def time_passed(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string



