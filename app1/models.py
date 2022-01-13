from django.contrib.auth.models import UserManager
from django.db import models
from django.utils import timezone


class Base(models.Model):
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CustomUserManager(UserManager):
    def get_query_set(self):
        return super(CustomUserManager, self).get_query_set().filter(is_delete=False)


# Create your models here.
class Merchant(Base):
    created_at = models.DateTimeField(default=timezone.localtime(timezone.now()))
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    mo_number = models.CharField(max_length=1000)
    gst_number = models.CharField(max_length=1000,null=True)
    code = models.CharField(max_length=100, null=True)

    objects = CustomUserManager


# Create your models here.
class Product(Base):
    created_at = models.DateTimeField(default=timezone.localtime(timezone.now()))
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="static/uploadedphoto")
    code = models.CharField(max_length=100, null=True)
    buy_price = models.FloatField(null=True)
    margin = models.FloatField(null=True)
    mrp = models.FloatField(null=True)
    sold_out = models.IntegerField(null=True)
    sell_price = models.FloatField(null=True)
    item = models.IntegerField(null=True)
    bill_no = models.CharField(max_length=100,null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="merchant_product")

    objects = CustomUserManager
