from django.urls import path
from main import views
from . import views

urlpatterns = [
    
    path('', views.todo_list, name="todo_list"),
    path('completed_todo_list/', views.completed_todo_list, name="completed_todo_list"),
    path('delete_task/<list_id>', views.delete_task, name="delete_task"),
    path('delete_list', views.delete_list, name="delete_list"),
    path('done_task/<list_id>', views.done_task, name="done_task"),
    path('not_done_task/<list_id>', views.not_done_task, name="not_done_task"),
    path('edit_task/<list_id>', views.edit_task, name='edit_task'),
    path('home/', views.home, name='home'),
]