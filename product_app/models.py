from django.db import models

# Create your models here.
class Products(models.Model):
    prod_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    Image = models.ImageField(upload_to = 'media',null=True,blank =True)

    class Meta:
        db_table = "product"
