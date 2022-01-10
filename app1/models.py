from django.contrib.auth.models import UserManager
from django.db import models


class Base(models.Model):
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CustomUserManager(UserManager):
    def get_query_set(self):
        return super(CustomUserManager, self).get_query_set().filter(is_delete=False)


# Create your models here.
class Video(Base):
    created_at = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to="static/uploadedphoto")
    code = models.CharField(max_length=100,null=True)

    objects = CustomUserManager
