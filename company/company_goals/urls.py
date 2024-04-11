from django.urls import path, include
from rest_framework import routers
from .views import CompanyGoalViewSet

router = routers.DefaultRouter()
router.register(r'company-goals', CompanyGoalViewSet)

urlpatterns = router.urls
