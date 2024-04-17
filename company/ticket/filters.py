import django_filters
from buying_tickets.models import Ticket
from .models import Ticket

class TicketFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Ticket
        fields = ['from_country','to_country','from_date','to_date']