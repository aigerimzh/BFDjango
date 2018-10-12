from django.urls import path
from main import views
from . import views

urlpatterns = [
    
    path('', views.my_blog, name="my_blog"),
    path('posted/', views.posted, name="posted"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('comment_post/<int:pk>', views.add_comment_to_post, name='add_comment_to_post'),
    path('delete_com/<int:pk>', views.delete_com, name='delete_com'),
    
]