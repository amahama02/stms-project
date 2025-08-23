from django.db import models
# Create your models here.
    
class Road(models.Model):
    name = models.CharField(max_length=200)
    length_km = models.IntegerField()
    
class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10, unique=True)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6)
    speed = models.IntegerField()
    road = models.ForeignKey(Road, on_delete=models.CASCADE)
