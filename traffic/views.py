from django.shortcuts import render
from .models import Road

# Create your views here.
def road_list(request):
    roads = Road.objects.all()
    context = {'roads': roads}
    return render(request, 'traffic/road_list.html', context)
