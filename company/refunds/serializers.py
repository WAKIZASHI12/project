from rest_framework import serializers
from django.utils import timezone

class RefundSerializer(serializers.Serializer):
    trip_start_date = serializers.DateTimeField()

    def validate_trip_start_date(self, value):
        if timezone.now() + timezone.timedelta(hours=48) > value:
            raise serializers.ValidationError("Refund request should be made at least 48 hours before the trip starts.")
        return value

def save(self):
    trip_start_date = self.validated_data['trip_start_date']
    cost = 0.8 * 100  # Base cost is 100 for this example.
    return cost
