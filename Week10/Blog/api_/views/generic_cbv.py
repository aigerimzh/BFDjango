from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from api_.serializers import ListModelSerializer
from api_.serializers import UserSerializer
from main.models import List
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(generics.RetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = List.objects.all()
    serializer_class = ListModelSerializer
    lookup_field = 'list_id'

class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class GenericTaskList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return List.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GenericTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'list_id'

    def get_object(self):
        return List.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return List.objects.for_user(self.request.user)