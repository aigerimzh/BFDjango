from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import RestaurantForm


def add_rest(request):
	if request.method == 'POST':
		form = RestaurantForm(request.POST or None)
		if form.is_valid():
			form.save()
			all_rest = Restaurant.objects.all
			return render(request, 'add_rest.html', {'all_rest': all_rest})
	else:
		all_rest = Restaurant.objects.all
		return render(request, 'add_rest.html', {'all_rest': all_rest})


def rest_list(request):
	all_rest = Restaurant.objects.all
	return render(request, 'rest_list.html', {'all_rest': all_rest})

def rest_detail(request, pk):
	item = Restaurant.objects.get(pk=pk)
	return render(request, 'rest_detail.html', {'item': item})

def del_rest(request, pk):
	item = Restaurant.objects.get(pk=pk)
	item.delete()
	return redirect('rest_list')

def edit_rest(request, pk):
    item = Restaurant.objects.get(pk=pk)

    if request.method == "POST":
        form = RestaurantForm(request.POST,instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('rest_detail',pk=item.pk)
    else:
        form = RestaurantForm(instance=item)

    return render(request, 'edit_rest.html', {'form': form})