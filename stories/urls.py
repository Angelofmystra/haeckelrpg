from django.conf.urls import patterns, url

from stories import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.index, name='stories'),
	# ex: /polls/1/
	url(r'^(?P<story_id>\d+)/$', views.detail, name='detail'),
)
