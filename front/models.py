from django.db import models
from django.utils.timezone import now

# Create your models here.
class StrainData(models.Model):
    date_time = models.DateTimeField(default=now)
    test_method_1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_3 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_4 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_5 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_6 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_7 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_8 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_9 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_10 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_11 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_12 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_13 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_14 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_15 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_16 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_17 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_18 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_19 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_20 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_21 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_22 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_23 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_24 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_25 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_26 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_27 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_28 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_29 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_30 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_31 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_32 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_33 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_34 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_35 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_36 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_37 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_38 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_39 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_40 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_41 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_42 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_43 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_44 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_45 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_46 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_47 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_48 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_49 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_50 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    def __str__(self):
        return str(self.date_time)

    class Meta:
        managed = True
        db_table = 'strain_data'
        verbose_name_plural = 'strain_data'


class TiltData(models.Model):
    date_time = models.DateTimeField(default=now)
    test_method_1 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_2 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_3 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_4 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_5 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_6 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_7 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_8 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_9 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_10 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_11 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_12 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_13 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_14 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_15 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_16 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_17 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_18 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_19 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_20 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_21 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_22 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_23 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_24 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_25 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_26 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_27 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_28 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_29 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_30 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_31 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_32 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_33 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_34 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_35 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_36 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_37 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_38 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_39 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    test_method_40 = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)

    def __str__(self):
        return str(self.date_time)

    class Meta:
        managed = True
        db_table = 'tilt_data'
        verbose_name_plural = 'tilt_data'


# class DisplacementData(models.Model):
#     date_time = models.DateTimeField(default=now)
#     test_method_1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_3 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_4 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_5 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_6 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_7 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_8 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_9 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_10 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_11 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_12 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_13 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_14 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_15 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_16 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_17 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_18 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_19 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_20 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_21 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_22 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_23 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_24 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_25 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#
#     def __str__(self):
#         return str(self.date_time)
#
#     class Meta:
#         managed = True
#         db_table = 'displacement_data'
#         verbose_name_plural = 'displacement_data'


class Settlement_PData(models.Model):
    date_time = models.DateTimeField(default=now)
    test_method_1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_3 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_4 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_5 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_6 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_7 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_8 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_9 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_10 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_11 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_12 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_13 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_14 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_15 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_16 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_17 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_18 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_19 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_20 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    def __str__(self):
        return str(self.date_time)

    class Meta:
        managed = True
        db_table = 'settlement_p_data'
        verbose_name_plural = 'settlement_p_data'


class Settlement_FData(models.Model):
    date_time = models.DateTimeField(default=now)
    test_method_1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_3 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_4 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_5 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_6 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_7 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_8 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_9 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_10 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_11 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_12 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_13 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_14 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_15 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_16 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_17 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_18 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_19 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    test_method_20 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    def __str__(self):
        return str(self.date_time)

    class Meta:
        managed = True
        db_table = 'settlement_f_data'
        verbose_name_plural = 'settlement_f_data'



# class VibrationData(models.Model):
#     date_time = models.DateTimeField(default=now)
#     test_method_1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_3 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_4 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_5 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_6 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_7 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_8 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_9 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_10 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_11 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_12 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_13 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_14 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_15 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_16 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_17 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_18 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_19 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_20 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_21 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_22 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_23 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_24 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#     test_method_25 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
#
#     def __str__(self):
#         return str(self.date_time)
#
#     class Meta:
#         managed = True
#         db_table = 'vibration_data'
#         verbose_name_plural = 'vibration_data'


