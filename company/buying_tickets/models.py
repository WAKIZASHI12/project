from django.db import models

class Ticket(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    seats_available = models.IntegerField()