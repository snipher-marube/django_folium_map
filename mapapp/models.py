from django.db import models

class Carbon(models.Model):
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    year = models.IntegerField()
    annual_co2_emissions_tonnes = models.DecimalField(max_digits=20, decimal_places=8)
    
    def __str__(self):
        return str(self.country)
    
    class Meta:
        verbose_name_plural = 'Carbon'
        ordering = ('country',)
