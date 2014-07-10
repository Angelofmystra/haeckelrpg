from django.shortcuts import render
from django.template import RequestContext

def index(request):
	return render(request, 'stories/stories.html')
def detail(request, story_id):
	return render(request, 'stories/story%s.html' % story_id)