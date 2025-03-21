from django.shortcuts import render

# Create your views here
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def buildingMuscle(request):
    return render(request, 'building_muscle.html')
def advanced_workout_routines(request):
    return render(request, 'advanced_workout_routines.html')