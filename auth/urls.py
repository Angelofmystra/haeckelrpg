from django.conf.urls import patterns, url

from auth import views

urlpatterns = patterns('',
	url(r'^login/', 'auth.sites.views.mylogin'),
	url(r'^logout/', 'auth.sites.views.mylogout'),

)