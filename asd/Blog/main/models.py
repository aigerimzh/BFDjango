from django.db import models
from datetime import datetime

class Blog(models.Model):
	tit_bl =  models.CharField(max_length=200)
	createted_at = models.DateTimeField(default=datetime.now, blank=True)
	text_bl = models.CharField(max_length=500)
	
	def __str__(self):
		return self.tit_bl + ' | '  + str(self.createted_at) +' | ' + self.text_bl
		
		
class Comment(models.Model):
    com_id = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=200)
    text_com = models.TextField()

    def __str__(self):
        return self.user + ' | '  + str(self.created_date) +' | ' + self.text_com