from django.shortcuts import render
from .models import Place, Movie, Date
import datetime
# Create your views here.
#def index(request):
    #return render(request, 'movie/index.html')

def page2index(request):
    return render(request, 'movie/page2-index.html')

def page21(request):
    today = datetime.date.today()
    tomorrow= today + datetime.timedelta(days=1)
    twodays= today + datetime.timedelta(days=2)
    threedays = today + datetime.timedelta(days=3)
    return render(request,'movie/page2-1.html',{"today":today, "tomorrow":tomorrow, "twodays":twodays,"threedays":threedays })

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