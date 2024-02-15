from django.db import models

# Create your models here.

class Contact(models.Model):
    # contact_id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    desc  = models.TextField(max_length=500)
    phonenumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name  = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_desc  = models.TextField(max_length=500)
    product_category    = models.CharField(max_length=50, default="")
    product_subcategory = models.CharField(max_length=50, default="")

    product_image = models.ImageField(upload_to="images/images")


    def __str__(self):
        return self.product_name