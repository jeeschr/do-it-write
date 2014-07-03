from django.conf.urls import patterns, url, include
from writing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^story/$', views.story, name="story"),
    url(r'^story/characters/$', views.characters, name="characters"),
    url(r'^story/events/$', views.events, name="events"),
    url(r'^story/text/$', views.text, name="text"),
)

urlpatterns += patterns('',
	(r'^tinymce/', include('tinymce.urls')),
)