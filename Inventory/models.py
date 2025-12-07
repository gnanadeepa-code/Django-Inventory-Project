from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0, null=True)
    description = models.TextField(max_length=500,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    gst = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
   # file = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.name
