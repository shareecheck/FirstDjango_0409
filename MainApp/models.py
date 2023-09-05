from django.db import models

# Create your models here.

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 

    def __repr__(self):
        return f'Item(name={self.name}, brand={self.brand}, count={self.count})'