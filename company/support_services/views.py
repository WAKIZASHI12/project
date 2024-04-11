from rest_framework import viewsets
from .models import SupportRequest
from .serializers import SupportRequestSerializer

class SupportRequestViewSet(viewsets.ModelViewSet):
    queryset = SupportRequest.objects.all()
    serializer_class = SupportRequestSerializer