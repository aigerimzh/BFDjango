from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ["r_name", "tel", "city", "created_by"]