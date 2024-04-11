from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CompanyGoal
from .serializers import CompanyGoalSerializer

class CompanyGoalViewSet(viewsets.ModelViewSet):
    queryset = CompanyGoal.objects.all()
    serializer_class = CompanyGoalSerializer
