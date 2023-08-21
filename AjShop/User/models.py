from django.db import models
from Admin.models import Product,UserInfo
from datetime import datetime 
# Create your models here.

class Mycart(models.Model):
    user = models.ForeignKey(to= 'Admin.UserInfo',
                            on_delete=models.CASCADE)
    
    gadget = models.ForeignKey(to= 'Admin.Product',
                            on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "Mycart"

class Ordermaster(models.Model):
    user = models.ForeignKey(to= 'Admin.UserInfo',
                            on_delete=models.CASCADE)
    amount = models.FloatField(default=1000)
    dateOfOrder = models.DateTimeField(default=datetime.now)
    details = models.CharField(max_length=200)
    class Meta:
        db_table = "Order"