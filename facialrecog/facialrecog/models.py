from django.db import models

# Create your models here.

class Attend(models.Model):
    name = models.CharField(max_length=1000)
    confidence = models.CharField(max_length=1000) 
    now = models.TextField(max_length=1000) 
    
    def __str__(self):
        return self.name