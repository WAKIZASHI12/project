# support_services/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import SupportRequestViewSet

router = routers.DefaultRouter()
router.register(r'support_requests', SupportRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]