from django import forms
from .models import List
from .models import ListCompl

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ["item","createted_at","completed","due"]

class ListComplForm(forms.ModelForm):
	class Meta:
		model = ListCompl
		fields = ["item","createted_at","completed"]