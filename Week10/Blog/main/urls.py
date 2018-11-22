from django.urls import path
from .views import ArticlList
from .views import CommentList
from .views import ArticleDetail
from .views import ArticleDelete
from .views import ArticleUpdate
from .views import ArticleCreate
from .views import CommentCreate
from .views import CommentDelete
from main.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/posted/', ArticlList.as_view(), name='blog_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='blog_detail'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='blog_delete'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='blog_update'),
    path('article/create/', ArticleCreate.as_view(), name='blog_create'),
    path('comment/<int:pk>/', CommentCreate.as_view(), name='comment_create'),
    path('comment/list/', CommentList.as_view(), name='comment_list'),
    path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
]