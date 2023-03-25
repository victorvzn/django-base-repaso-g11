from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url_image = models.TextField()
    price = models.FloatField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products'
