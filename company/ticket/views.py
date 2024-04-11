from rest_framework.generics import ListAPIView
from .models import Ticket
from .serializers import TicketSerializer


class TicketListView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer