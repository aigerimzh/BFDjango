from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Restaurant
from .forms import RestaurantForm 

def home(request):
    return render(request, 'home.html')


def add_rest(request):
	
	if request.method == 'POST':
		form = RestaurantForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('rest_list')
	else:
		form = RestaurantForm()
	context = {
		'form': form
	}	
	return render(request, 'add_rest.html', context)




def rest_list(request):
	rest = Restaurant.objects.all()
	context = {
		'rest': rest
	}
	return render(request, 'rest_list.html', context)

class Rest_detail(View):
	def get(self,request,pk):
		item = Restaurant.objects.get(pk=pk)
		context = {
			'item' : item

		}
		return render(request, 'rest_detail.html', context)



def del_rest(request,pk):
		item = Restaurant.objects.get(pk=pk)
		item.delete()
		return redirect('rest_list')

@login_required
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