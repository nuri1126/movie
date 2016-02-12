from django.shortcuts import render
from .models import Place, Movie, Date, Key
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
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
    filtered_list = Key.objects.all()
    query_filtered= request.GET.get('filtered')
    if query_filtered:
        filtered_list=filtered_list.filter(
            Q(movie__title__icontains=query_filtered)|
            Q(place__name__icontains=query_filtered)).distinct()
    else:
        pass

    return render(request,'movie/page2-3.html',{'filtered_list':filtered_list})

def page24(request):
    selected_values = request.GET.getlist('test')
    return render(request,'movie/page2-4.html')

def index(request):

    movies = Movie.objects.all()
    movies = Movie.objects.order_by('title')
    params = {'movies': movies}
    return render(request, 'movie/index.html', params)