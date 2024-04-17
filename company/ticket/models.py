from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
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






class TicketReserve (models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    seat = models.IntegerField(default=0, unique=True)