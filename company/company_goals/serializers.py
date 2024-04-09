from rest_framework import serializers
from .models import CompanyGoal

class CompanyGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyGoal
        fields = '__all__' 
        