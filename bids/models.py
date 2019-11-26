from django.db import models
from django.contrib.auth.models import User
from auction.models import Auction

# Create your models here.

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()
    
    
    def __str__(self):
        return "(" + self.user_id + ", " + self.auction_id + ", " + self.bid_time + ")"