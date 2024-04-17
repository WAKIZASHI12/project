from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from django_filters import rest_framework as filters
from .models import Ticket, TicketReserve
from .filters import TicketFilter
from .serializers import TicketSerializer, TicketReserveSerializer

class TicketListView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TicketFilter

class TicketRetrieveView(RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketReserverCreateAPIView(CreateAPIView):
    queryset = TicketReserve.objects.all()
    serializer_class = TicketReserveSerializer
    permission_classes = [permissions.IsAuthenticated]
    