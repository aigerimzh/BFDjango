from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from main.models import List
from main.forms import ListForm
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
	template_name = 'home.html'
	http_method_names = ['get']


class ToDoList(ListView):
	model = List
	context_object_name = 'td_list'

class ComplList(ListView):
	model = List
	context_object_name = 'compl_list'
	template_name_suffix = 'compl_list_list'

class TaskDelete(DeleteView, LoginRequiredMixin):
	model = List
	success_url = reverse_lazy('list_list')

	def get_queryset(self):
		return List.objects.for_user(user=self.request.user)

class TaskUpdate(UpdateView, LoginRequiredMixin):
	model = List
	form_class = ListForm
	success_url = reverse_lazy('list_list')
	template_name_suffix = '_update_form'

	def get_queryset(self):
		return List.objects.for_user(user=self.request.user)

class TaskCreate(CreateView, LoginRequiredMixin):
	model = List
	success_url = reverse_lazy('list_list')
	fields = ["item","due","owner"]

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)


class Done_task(View):
	#@login_required
	def get(self,request,list_id):
		#item = List.objects.filter(user = request.user)
		item = List.objects.get(pk=list_id)
		if item.completed:
			item.completed = False
		else:
			item.completed = True
		item.save()
		return redirect('list_list')

class Not_done_task(View):
	def get(self,request,list_id):
		item = List.objects.get(pk=list_id)
		if item.completed:
			item.completed = False
		else:
			item.completed = True
		item.save()
		return redirect('compl_list')
