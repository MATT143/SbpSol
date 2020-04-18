from django.db import models
from django.utils.timezone import datetime



# Create your models here.
class com_order_mapper(models.Model):
    subRefId=models.CharField(max_length=20,unique=True)
    salesOrderNo=models.CharField(max_length=20,unique=True)
    offerName=models.CharField(max_length=20)
    quantity=models.IntegerField(default=100)
    subscriptionId=models.CharField(max_length=20,default=None,null=True)
    lineStatus=models.IntegerField(blank=True,default=32)
    requestedStartDate=models.DateField(default='1990-10-28')
    creationDate=models.DateTimeField(default=datetime.now())
    deliveryMethod=models.CharField(max_length=30,default=None,null=True)
    initialTerm=models.IntegerField(blank=True,default=12)
    autoRenewalFlag=models.BooleanField(default=True)
    tfEligible=models.BooleanField(default=False)
    prov_email=models.EmailField(default='na@na.com')


    def __str__(self):
        return self.salesOrderNo