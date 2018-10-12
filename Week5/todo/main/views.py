from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import List
from .models import ListCompl
from .forms import ListForm
from .forms import ListComplForm
from django.contrib import messages
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def completed_todo_list(request):
	all_items = List.objects.all
	return render(request, 'completed_todo_list.html', {'all_items': all_items})

def todo_list(request):
    if request.method == 'POST':
    	form = ListForm(request.POST or None)

    	if form.is_valid():
    		form.save()
    		all_items = List.objects.all
    		all_items_com = ListCompl.objects.all
    		return render(request,'todo_list.html',{'all_items': all_items})

    else:
    	all_items = List.objects.all
    	return render(request, 'todo_list.html', {'all_items': all_items})

def delete_task(request,list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	return redirect('todo_list')

def delete_list(request):
	List.objects.all().delete()
	return redirect('todo_list')

def edit_task(request, list_id):
    item = List.objects.get(pk=list_id)

    if request.method == "POST":
        form = ListForm(request.POST,instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('todo_list')
    else:
        form = ListForm(instance=item)

    return render(request, 'edit_task.html', {'form': form})

def done_task(request,list_id):
	item = List.objects.get(pk=list_id)
	if item.completed:
		item.completed = False
	else:
		item.completed = True

	item.save()
	
	return redirect('todo_list')

def not_done_task(request, list_id):
	item = List.objects.get(pk=list_id)
	if item.completed:
		item.completed = False
	else:
		item.completed = True

	item.save()
	
	return redirect('completed_todo_list')

