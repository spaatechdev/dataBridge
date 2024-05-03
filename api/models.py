from django.db import models
from django.utils.timezone import now
import pytz

class SensorType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'sensor_types'
        verbose_name_plural = 'sensor_types'

class Sensor(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE, blank=True, null=True)
    max = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    min = models.DecimalField(max_digits=20, decimal_places=10, default=0)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'sensors'
        verbose_name_plural = 'sensors'


class Section(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'sections'
        verbose_name_plural = 'sections'


class Section_Sensor_Mapping(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        managed = True
        db_table = 'section_sensor_mappings'
        verbose_name_plural = 'section_sensor_mappings'


class Time_Stamp(models.Model):
    date_time = models.DateTimeField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        managed = True
        db_table = 'time_stamps'
        verbose_name_plural = 'time_stamps'

class Sensor_Data(models.Model):
    section_sensor_mapping=models.ForeignKey(Section_Sensor_Mapping, on_delete=models.CASCADE, blank=True, null=True)
    time_stamp = models.ForeignKey(Time_Stamp, on_delete=models.CASCADE, blank=True, null=True)
    data=models.DecimalField(max_digits=40, decimal_places=20, blank=True, null=True)

    def __str__(self):
        return str(self.data)

    class Meta:
        managed = True
        db_table = 'sensor_datas'
        verbose_name_plural = 'sensor_datas'