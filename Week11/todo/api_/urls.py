from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import generic_cbv

#router = routers.DefaultRouter()
#router.register('tasks/', generic_cbv.TaskViewSet)
urlpatterns = [

    path('students/', generic_cbv.TaskViewSet.as_view()),


    # path('post/comments/', views.CommentCreate.as_view()),
    # path('post/<int:post_id>/comments/', views.CommentDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

#urlpatterns = router.urls