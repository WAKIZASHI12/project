from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RefundSerializer

@api_view(['POST'])
def refund_view(request):
    serializer = RefundSerializer(data=request.data)
    if serializer.is_valid():
        cost = serializer.save()
        return Response({'cost': cost}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)