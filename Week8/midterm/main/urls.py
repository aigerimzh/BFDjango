from django.urls import path
from main import views
from . import views
from main.views import Rest_detail


urlpatterns = [
	path('', views.home, name='home'),
	path('add_rest', views.add_rest, name = "add_rest"),
	path('rest_list', views.rest_list, name = "rest_list"),
	path('rest_detail/<int:pk>', Rest_detail.as_view(), name="rest_detail"),
	path('del_rest/<int:pk>', views.del_rest, name="del_rest"),	
	path('edit_rest/<int:pk>', views.edit_rest, name="edit_rest"),		
]