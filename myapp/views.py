from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from  django.utils import timezone
from myapp.models import Todo

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'main/index.html', {"todo_items" : todo_items})

def add_todo(request):
    print(request.POST)
    response = "I am called"
    current_date = timezone.now()
    content = request.POST["content"]
    priority = request.POST["priority"]
    if(content and priority):
        created_obg = Todo.objects.create(added_date=current_date, text=content, priority=priority)
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")