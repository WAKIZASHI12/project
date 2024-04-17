from rest_framework import serializers
from .models import Ticket, TicketReserve
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

class TicketReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketReserve
        fields = "__all__"