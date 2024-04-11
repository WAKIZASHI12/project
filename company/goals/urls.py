from django.urls import path
from.views import GoalViewSet

urlpatterns = [
    path('', GoalViewSet.as_view({'get': 'list', 'post': 'create'}), name='goal-list'),
    path('<int:pk>/', GoalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='goal-detail'),
]