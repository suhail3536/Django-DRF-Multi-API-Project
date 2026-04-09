from django.db import models

# Create your models here.
class Worker(models.Model):
    worker_id =models.CharField(max_length=20)
    Worker_name =models.CharField(max_length=50)
    post =models.CharField(max_length=30)
     
    def _strr_(self):
          return self.Worker_name
