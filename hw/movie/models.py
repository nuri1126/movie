from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=100,verbose_name='이름',help_text='help_text!')
    movie=models.ManyToManyField('Movie',through='Key')
    date=models.ManyToManyField('Date',through='Key')
    #urlfield도 있음
    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=100)
    date=models.ManyToManyField('Date',through='Key')
    def __str__(self):
        return self.title

class Date(models.Model):
    day=models.CharField(max_length=100)
    def __str__(self):
        return self.day

class Key(models.Model):
    movie=models.ForeignKey(Movie)
    place=models.ForeignKey(Place)
    date=models.ForeignKey(Date)

    def __str__(self):
        #return "{}/{}/{}".format(self.movie,self.place,self.date)
        return str(self.movie)+" / "+str(self.place)+" / "+str(self.date)
'''
class Time(models.Model):
    time=models.CharField(max_length=100)
    def __str__(self):
        return self.time
'''
class Time(models.Model):
    moviekey=models.ForeignKey(Key)
    time=models.CharField(max_length=100)
    def __str__(self):
        return str(self.moviekey)+" / "+str(self.time)

class MovieInfo(models.Model):
    timeInfo=models.ForeignKey(Time)
    def __str__(self):
        return str(self.timeInfo)

from django.contrib.auth.models import User
'''
class Profile(models.Model):
    user=models.OneToOneField(User)
'''