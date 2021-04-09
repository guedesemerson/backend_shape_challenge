from django.db import models
from vessel.models import Vessel


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    equipment_code = models.CharField(unique=True, verbose_name='Equipment Code', max_length=8)
    location = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"

    def __str__(self):
        return self.name