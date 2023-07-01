from django.db import models

# Create your models here.
class CsvData(models.Model):
    time = models.CharField(max_length=100, blank=True, null=True)
    method_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method_3 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method_4 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method_5 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method_6 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method_7 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method_8 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method_9 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    method_10 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    calculated_time = models.TimeField(blank=True, null=True)
    hour_slab = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.time

    class Meta:
        managed = True
        db_table = 'csv_data'
        verbose_name_plural = 'csv_data'