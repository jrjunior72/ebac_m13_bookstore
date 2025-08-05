from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User

from product.models import Product 

class Order(models.Model): 
    product = models.ManyToManyField(Product, blank=False, null=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("completed", "Completed"), ("cancelled", "Cancelled")],
        default="pending"
    )
    created_at = models.DateTimeField(default=timezone.now)
