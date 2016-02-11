import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw.settings')

import django
django.setup()

from movie.models import Movie, Place
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://www.google.co.kr/movies')
soup = BeautifulSoup(html)
title_tags = soup.find_all("div","name","a")
place_tags = soup.find_all("h2","name","a")


for title_tag in title_tags:
	title = title_tag.text
	print (title)
	movie, is_created = Movie.objects.get_or_create(title=title)
	movie.save()
print('total movie : {}'.format(Movie.objects.all().count()))
for place_tag in place_tags:
	place = place_tag.text
	print (place)
	place, is_created = Place.objects.get_or_create(name=place)
	place.save()
print('total place : {}'.format(Place.objects.all().count()))
