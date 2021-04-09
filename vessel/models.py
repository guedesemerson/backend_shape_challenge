from django.db import models


class Vessel(models.Model):
    vessel_code = models.CharField(unique=True, max_length=5)

    class Meta:
        verbose_name = "Vessel"
        verbose_name_plural = "Vessels"

    def __str__(self):
        return self.vessel_code