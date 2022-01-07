from django.contrib.auth.models import UserManager
from django.db import models


class CustomUserManager(UserManager):
    def get_query_set(self):
        return super(CustomUserManager, self).get_query_set().filter(is_delete=False)


# Create your models here.
class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to="static/uploadedphoto")
    links = models.CharField(max_length=10000)

    objects = CustomUserManager
