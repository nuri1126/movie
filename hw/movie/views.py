from django.shortcuts import render
from .models import Place, Movie, Date

# Create your views here.
#def index(request):
    #return render(request, 'movie/index.html')

def index2(request):
    return render(request, 'movie/index2.html')

def page1(request):
    dates = Date.objects.all
    return render(request,'movie/page1.html',{"dates":dates})

def page2(request):
    places = Place.objects.all
    return render(request,'movie/page2.html',{"places":places})

def page3(request):
	return render(request,'movie/page3.html')

def page4(request):
    return render(request,'movie/page4.html')

def index(request):
    movies = Movie.objects.all()
    params = {'movies': movies}
    return render(request, 'movie/index.html', params)