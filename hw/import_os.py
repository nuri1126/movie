import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw.settings')

import django
django.setup()

from movie.models import Movie
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://www.google.co.kr/movies')
soup = BeautifulSoup(html)
title_tags = soup.find_all("div","name","a")


for title_tag in title_tags:
	print (title_tag)
	title = title_tag.text
	movie, is_created = Movie.objects.get_or_create(title=title)
	movie.save()

print('total movie : {}'.format(Movie.objects.all().count()))
