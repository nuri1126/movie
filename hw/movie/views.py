from django.shortcuts import render
from .models import Place, Movie, Date

# Create your views here.
#def index(request):
    #return render(request, 'movie/index.html')

def page2index(request):
    return render(request, 'movie/page2-index.html')

def page21(request):
    dates = Date.objects.all
    return render(request,'movie/page2-1.html',{"dates":dates})

def page22(request):
    places = Place.objects.all
    return render(request,'movie/page2-2.html',{"places":places})

def page23(request):
	return render(request,'movie/page2-3.html')

def page24(request):
    return render(request,'movie/page2-4.html')

def index(request):
    movies = Movie.objects.all()
    movies = Movie.objects.order_by('title')
    params = {'movies': movies}
    return render(request, 'movie/index.html', params)