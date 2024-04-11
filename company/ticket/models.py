from django.db import models

# Create your models here.
class Ticket(models.Model):
    from_country = models.CharField(max_length=256)
    to_country = models.CharField(max_length=256)
    from_time = models.TimeField()
    to_time = models.TimeField()
    from_place = models.CharField(max_length=256)
    to_place = models.CharField(max_length=256)
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.PositiveIntegerField()
