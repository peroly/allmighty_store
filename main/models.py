import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('soccer ball', 'Soccer Ball'),
        ('jersey shirt', 'Jersey Shirt'),
        ('others', 'Others'),
    ]
    
    #model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    product_views = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    # @property
    # def is_news_hot(self):
    #     return self.news_views > 20
        
    # def increment_views(self):
    #     self.product_views += 1
    #     self.save()