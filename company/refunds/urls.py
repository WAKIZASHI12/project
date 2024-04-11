from django.urls import path
from . import views

urlpatterns = [
    path('refund/', views.refund_view, name='refund'),
]