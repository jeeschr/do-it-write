from django.conf.urls import patterns, url, include
from writing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^story/$', views.story, name="story"),
)

urlpatterns += patterns('',
	(r'^summernote/', include('django_summernote.urls')),
)