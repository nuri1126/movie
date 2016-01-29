"""hw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'movie.views.index'),
    url(r'^index.html/$', 'movie.views.index'),
    url(r'^page2-index.html/page2-1.html/$', 'movie.views.page21'),
    url(r'^page2-index.html/page2-2.html/$', 'movie.views.page22'),
    url(r'^page2-index.html/page2-3.html/$', 'movie.views.page23'),
    url(r'^page2-index.html/page2-4.html/$', 'movie.views.page24'),
    url(r'^page2-index.html/$', 'movie.views.page2index'),
    ]
