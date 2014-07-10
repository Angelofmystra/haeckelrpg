from django.conf.urls import patterns, include, url
from home import views
from django.contrib import admin
from django.conf import settings # for the image
from django.conf.urls.static import static # for the image
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('home.urls', namespace="home")), #raw interpolation of a string  is r, $ is end here, and ^ is start here
    # url(r'^blog/', include('blog.urls')),
    url(r'^todolist/', include('todolist.urls', namespace="todolist")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^game/', include('game.urls', namespace="game")),
	url(r'^stories/', include('stories.urls', namespace="stories")),
	url(r'^login/', 'auth.views.mylogin'),
	url(r'^logout/', 'auth.views.mylogout'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #remove for production