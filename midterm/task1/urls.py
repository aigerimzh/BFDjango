from django.urls import path
from task1 import views
from . import views

urlpatterns = [

	path('add_rest', views.add_rest, name = "add_rest"),
	path('rest_list', views.rest_list, name = "rest_list"),
	path('rest_detail/<int:pk>', views.rest_detail, name="rest_detail"),
	path('del_rest/<int:pk>', views.del_rest, name="del_rest"),
	path('edit_rest/<int:pk>', views.edit_rest, name="edit_rest"),

]