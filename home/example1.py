from django.shortcuts import render_to_response
from django.template import RequestContext
from beers.models import Beer

def BeersAll(request):
    beers = Beer.objects.all().order_by('name')
    context = {'beers': beers} # Takes the list of all beer objects ordered by name and puts it inside a variable called beers, which is passed to the template, so the template can then call the return from the line above. 
    return render_to_response('beersall.html', context, context_instance=RequestContext(request)) #creates a http response with all the information included, which is the context, and passes it back to the browser, so you get a valid web response. 
    # Everything through the user is going to be passed, allows the user to move from page to page, such as their identity. We dont need it immediately since nobody is logging in, but its good practice to use.