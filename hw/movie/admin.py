from django.contrib import admin
from movie.models import Place, Date, Time, Key, Movie, MovieInfo
# Register your models here.
class KeyAdmin(admin.ModelAdmin):
    list_display=['movie','date','place']
class PlaceAdmin(admin.ModelAdmin):
    list_display=['name']
class MovieAdmin(admin.ModelAdmin):
    list_display=['title']
class DateAdmin(admin.ModelAdmin):
    list_display=['day']
class TimeAdmin(admin.ModelAdmin):
    list_display=['moviekey','time']
class MovieInfoAdmin(admin.ModelAdmin):
	list_display=['timeInfo']




admin.site.register(Key,KeyAdmin)
admin.site.register(Place)
admin.site.register(Movie)
admin.site.register(Date)
admin.site.register(Time,TimeAdmin)
admin.site.register(MovieInfo,MovieInfoAdmin)