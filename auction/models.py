from django.db import models
from products.models import Product

# Create your models here.

class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_no = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField
    
    def __str__(self):
        return "(" + self.product_id + ", " + self.bid_no + ", " + self.start_time + ", " + self.end_time + ")"