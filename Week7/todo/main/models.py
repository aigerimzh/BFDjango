from django.db import models
from datetime import datetime

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	createted_at = models.DateTimeField(default=datetime.now, blank=True)
	due = models.DateField('Due Date', blank=True, null=True)

	def __str__(self):
		return self.item + ' | ' + str(self.createted_at) +' | ' + str(self.completed) +' | ' + str(self.due)


#dont need
class ListCompl(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	createted_at = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.item + ' | ' + str(self.createted_at) +' | ' + str(self.completed)



		
		