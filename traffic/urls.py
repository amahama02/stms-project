from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoadViewSet, VehicleViewSet, EventViewSet, TrafficDataViewSet

router = DefaultRouter()
router.register(r'roads', RoadViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'events', EventViewSet)
router.register(r'traffic_data', TrafficDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]