from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import ToDoItem
# Create your views here.

def index(request):
    all_items = ToDoItem.objects.all()
    return render(request,'index.html', {'all_items':all_items})

def addTodo(request):
    c = request.POST['content']
    new_item = ToDoItem(content = c)
    #save
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
   
    item_to_delete = ToDoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
