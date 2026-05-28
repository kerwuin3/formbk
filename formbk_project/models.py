from django.db import models

# Create your models here.
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)