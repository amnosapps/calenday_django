from django.db import models


# Create your models here.
class Schedule(models.Model):
    owner = models.CharField(max_length=120)
    guest = models.CharField(max_length=120)
    service = models.CharField(max_length=120)
    schedule = models.DateField()

    class Meta:
        verbose_name = ("Schedule")
        verbose_name_plural = ("Schedules")
