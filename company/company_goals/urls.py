from rest_framework import routers
from rest_framework import routers
from .views import CompanyGoalViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'company-goals', CompanyGoalViewSet)
