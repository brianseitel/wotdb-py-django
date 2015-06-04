"""wotdb URL Configuration

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
from wotdb_search import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^$',                          views.IndexView.as_view(),         name="index"),
    url(r'^book/(?P<pk>[0-9]+)/$',      views.BookView.as_view(),          name="chapter_list"),
    url(r'^chapter/(?P<pk>[0-9]+)/$',   views.ChapterView.as_view(),       name="chapter"),
    url(r'^character/$',                views.IndexView.as_view(),         name="character_list"),
    url(r'^character/(?P<pk>[0-9]+)/$', views.CharacterView.as_view(),     name="character"),
    url(r'^interview/$',                views.InterviewList.as_view(),     name="interview_list"),
    url(r'^interview/(?P<pk>[0-9]+)/$', views.InterviewDetail.as_view(),   name="interview"),
    url(r'^job/(?P<pk>[0-9]+)/$',       views.JobDetail.as_view(),         name="job"),
    url(r'^place/$',                    views.PlacesIndexView.as_view(),   name="places_index"),
    url(r'^place/(?P<pk>[0-9]+)/$',     views.PlaceView.as_view(),         name="place"),
    url(r'^pov/$',                      views.PointOfViewList.as_view(),   name="pov_list"),
    url(r'^pov/(?P<pk>[0-9]+)/$',       views.PointOfViewDetail.as_view(), name="pov"),
    url(r'^search/$',                   views.search, name="search"),
    url(r'^about/$',                    views.about,  name="about"),
    # url(r'^admin/', include(admin.site.urls)),
]
