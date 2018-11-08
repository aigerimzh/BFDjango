from django.db import models
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class TodoManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	objects=TodoManager()
	createted_at = models.DateTimeField(default=datetime.now, blank=True)
	due = models.DateTimeField('Due Date', blank=True, null=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)


	def __str__(self):
		return self.item + ' | ' + str(self.createted_at) +' | ' + str(self.completed) +' | ' + str(self.due)

	def get_absolute_url(self):
		return reverse_lazy('list_list')


#dont need
class ListCompl(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	createted_at = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.item + ' | ' + str(self.createted_at) +' | ' + str(self.completed)



		
		