from django.urls import path
from .views import ToDoList
from .views import TaskDelete
from .views import TaskUpdate
from .views import TaskCreate
from .views import ComplList
from main.views import Done_task
from main.views import Not_done_task
from main.views import HomeView
from .models import List 

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('td/<list_id>/done_task/', Done_task.as_view(), name="done_task"),
	path('cl/<list_id>/not_done_task/', Not_done_task.as_view(), name="not_done_task"),
    path('td/<int:pk>/update/', TaskUpdate.as_view(), name='list_update'),
    path('td/<int:pk>/delete/', TaskDelete.as_view(), name='list_delete'),
    path('td/', ToDoList.as_view(), name='list_list'),
    path('td/create/', TaskCreate.as_view(), name='task_create'),
    path('cl/', ComplList.as_view(), name='compl_list'),
]