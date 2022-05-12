from django.db import models

# Create your models here.
class UrlManage(models.Model):
    url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)