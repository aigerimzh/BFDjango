from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
	r_name = models.CharField(max_length = 200)
	tel = models.IntegerField()
	city = models.CharField(max_length = 100)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	def __srt__(self):
		return self.r_name + '|' + str(self.tel)  + '|' + self.city + '|' + str(self.created_by)