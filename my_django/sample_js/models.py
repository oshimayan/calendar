from django.db import models
from django.utils.timezone import now


class Carandar(models.Model):
    subject = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(default=now)
    all_day_flg = models.BooleanField(default=False)
    contents = models.CharField(max_length=1000)
