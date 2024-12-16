from django.db import models

# Create your models here.
class Salesdata(models.Model):
    country = models.CharField(max_length=100)
    sales = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Salesdata'
    
    def __str__(self):
        return f'{self.country}-{self.sales}'
