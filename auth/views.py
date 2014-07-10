from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth.views import HttpResponseRedirect
from django.contrib.auth.views import logout
# Create your views here.
def mylogin(request):
  if request.method == 'POST':
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
    	if user.is_active:
        	login(request, user)
        	# success
        	if request.POST['next']:
          		return HttpResponseRedirect(request.POST['next'])
        	else:
          		return HttpResponseRedirect('/')
      	else:
        	# disabled account
      		return direct_to_template(request, 'inactive_account.html')
    else:
    	# invalid login
    	return direct_to_template(request, 'invalid_login.html')
      
def mylogout(request):
  logout(request)
  return HttpResponseRedirect('/')
  #return direct_to_template(request, 'logged_out.html')
