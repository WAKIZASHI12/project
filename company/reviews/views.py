from rest_framework.generics import ListAPIView

from .serializers import ReviewSerializer
from .models import Review

class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer