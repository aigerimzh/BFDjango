from django.db import models


class Restaurant(models.Model):
	r_name = models.CharField(max_length = 200)
	tel = models.IntegerField()
	city = models.CharField(max_length = 100)
	def __srt__(self):
		return self.r_name + '|' + str(self.tel)  + '|' + self.city + '|' + str(self.user)