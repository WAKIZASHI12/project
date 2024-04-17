from django.urls import path
from ticket.serializers import TicketReserveSerializer
from .views import TicketListView, TicketRetrieveView, TicketReserverCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("tickets/", TicketListView.as_view()),
    path("tickets/reserve/", TicketReserverCreateAPIView.as_view()),
]



