from django.db import models
from django.conf import settings

class Road(models.Model):
    name = models.CharField(max_length=100, unique=True)
    length_km = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.license_plate

class Event(models.Model):
    EVENT_TYPES = [
        ('accident', 'Accident'),
        ('congestion', 'Congestion'),
        ('road_work', 'Road Work'),
        ('other', 'Other'),
    ]
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    description = models.TextField(blank=True, null=True)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_long = models.DecimalField(max_digits=9, decimal_places=6)
    road = models.ForeignKey('Road', on_delete=models.CASCADE, related_name='events')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event: {self.event_type} on {self.road.name}"

class TrafficData(models.Model):
    speed_kph = models.DecimalField(max_digits=6, decimal_places=2)
    position_lat = models.DecimalField(max_digits=9, decimal_places=6)
    position_long = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    road = models.ForeignKey('Road', on_delete=models.CASCADE, related_name='traffic_data')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='traffic_data')

    def __str__(self):
        return f"Data for {self.vehicle.license_plate} on {self.road.name}"