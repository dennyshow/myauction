from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from auction.models import Auction

# Create your models here.

class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    message = models.TextField()
    time_sent = models.DateTimeField()
    
    
    def __str__(self):
        return "(" + self.user_id + ", " + self.product_id + ", " + self.auction_id + ", " + self.message + ", " + self.time_sent + ")"