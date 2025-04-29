
# Create your models here.
from django.db import models

class Retailer(models.Model):
    name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    address = models.TextField(max_length=500)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
