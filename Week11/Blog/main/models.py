from django.db import models
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class TodoManager(models.Manager):
    def for_user(self, user):
        return self.filter(author=user)

class Blog(models.Model):
	tit_bl =  models.CharField(max_length=200)
	createted_at = models.DateTimeField(default=datetime.now, blank=True)
	text_bl = models.CharField(max_length=500)
	author = models.ForeignKey(User, on_delete=models.CASCADE,null = True )
	objects = TodoManager()
	def __str__(self):
		return self.tit_bl + ' | '  + str(self.createted_at) +' | ' + self.text_bl
	
	def get_absolute_url(self):
		return reverse_lazy('blog_list')	
		
class Comment(models.Model):
	com_id = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
	created_date = models.DateTimeField(default=datetime.now, blank=True)
	user = models.CharField(max_length=200)
	text_com = models.TextField()

	def get_absolute_url(self):
		return reverse_lazy('blog_list')

	def __str__(self):
		return self.user + ' | '  + str(self.created_date) +' | ' + self.text_com

		