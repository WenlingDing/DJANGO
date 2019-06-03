from django.db import models
from django.contrib.auth.models import User
from tracker_app.models import Feature
# # Create your models here.

# Create your models here.
class Order(models.Model):
    
    ordered_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name='orders')
    stripe_token = models.CharField(max_length=1000, blank=False)
    purchased_at = models.DateTimeField(blank=False)
    name = models.CharField(max_length=255, blank=False)
    address =models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return "Order - " + str(self.id)
    
class OrderLineItem(models.Model):
    
    post = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name = 'orders')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name = 'order_line_items')
    quantity = models.IntegerField()
    def __str__(self):
        return "Order {} - Product {}".format(self.order_id, self.post_id)