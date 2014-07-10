from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def index(request):
	#latest_todo_list = Todo.objects.all().order_by('priority')[:10]
	#context = {'todolist': latest_todo_list}
	return render(request, 'home/base2.html')