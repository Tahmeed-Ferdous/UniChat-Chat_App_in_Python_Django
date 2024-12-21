from django.db import models
from datetime import time
# Create your models here.

class User(models.Model):
    # THIS SHOULD BE COURSE WHY IS IT CALLED USER?

    name = models.CharField(max_length=100)
    task = models.CharField(max_length=255, default='New Task')
    title = models.CharField(max_length=128, default='Title')
    img = models.ImageField(upload_to='images/', default='def.png', null=True, blank=True)
    start_time=models.TimeField(max_length=100, null=True,blank=True)
    days= models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f'{self.name}: {self.task} {self.start_time} {self.days}'