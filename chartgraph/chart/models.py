from django.db import models

# Create your models here.


class Product(models.Model):
    category = models.CharField(max_length=255, null=False, blank=False)
    num_products = models.IntegerField()

    def __str__(self):
        return f'{self.category} - {self.num_products} products'