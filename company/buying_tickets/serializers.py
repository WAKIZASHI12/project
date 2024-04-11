from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'flight_number', 'departure_city', 'arrival_city', 'departure_time', 'arrival_time', 'price', 'seats_available']