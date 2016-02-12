import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw.settings')

import django
django.setup()

from django.core.files import File

from io import BytesIO
import requests
from movie.models import Movie, Place
# import urllib.request
from bs4 import BeautifulSoup

# html = urllib.request.urlopen('http://www.google.co.kr/movies')
html = requests.get('http://www.google.co.kr/movies').text
soup = BeautifulSoup(html)
title_tags = soup.find_all("div","name","a")
place_tags = soup.find_all("h2","name","a")

for title_tag in title_tags:
	title = title_tag.text
	print (title)
	movie, is_created = Movie.objects.get_or_create(title=title)
	# movie.save()  # 바뀐 것이 없으므로, save 는 의미가 없다.
	
	# poster_html = urllib.request.urlopen('http://www.google.co.kr/movies?q='+str(movie))
	poster_html = requests.get('http://www.google.co.kr/movies', {'q': str(movie)}).text
	poster_soup = BeautifulSoup(poster_html)
	poster_tags = poster_soup.find_all("div", "img", "img")
	# poster_soup.select('div img.myclass img')
	for poster_tag in poster_tags:
		image_tag = poster_tag.find('img')
		title = image_tag['alt']
		image_url = image_tag['src']
		if not image_url.startswith('http'):
			image_url = 'http:' + image_url
		image_filename = os.path.basename(image_url.split('?')[0])
		print(title)
		print(image_url)
		print(image_filename)
		r = requests.get(image_url, stream=True)
		image_data = b''.join(r)

		io = BytesIO()
		io.write(image_data)
		io.seek(0)

		# movie, is_created = Movie.objects.get_or_create(title=title)
		movie.poster.save(image_filename, File(io))

print('total movie : {}'.format(Movie.objects.all().count()))

for place_tag in place_tags:
	place = place_tag.text
	print (place)
	place, is_created = Place.objects.get_or_create(name=place)
	place.save()

print('total place : {}'.format(Place.objects.all().count()))


