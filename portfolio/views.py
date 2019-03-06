from django.shortcuts import render
from .models import Portfolio

def home(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'album.html', {'portfolios':portfolios})