from django.shortcuts import render
from .models import Solution, BODMAS

# Create your views here.
def home(request):
    return render(request, 'Homepage.html')

def solution(request):
    pass