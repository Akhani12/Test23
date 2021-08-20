from django.db import models


# Create your models here.
class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to="static/uploadedphoto")
    links = models.CharField(max_length=10000)
