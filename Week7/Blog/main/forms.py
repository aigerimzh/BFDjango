from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ["tit_bl","createted_at","text_bl"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user", "text_com"]