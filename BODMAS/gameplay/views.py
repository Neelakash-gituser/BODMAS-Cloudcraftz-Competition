from http.client import HTTPResponse
from django.shortcuts import render
from .models import Solution, BODMAS

# Create your views here.
def home(request):
    return render(request, 'Homepage.html')

def solution(request):
    obj = Solution()
    N1, O1, N2, O2, N3, N4 = obj.new_problem()
    context = {'N1': N1, 'O1': O1, 'N2': N2, 'O2': O2, 'N3': N3, 'N4': N4}
    return render(request, 'Gameplay.html', {'context': context})

def users(request):
    return render(request, 'Result.html')
