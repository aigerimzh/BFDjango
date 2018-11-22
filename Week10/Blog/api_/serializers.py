from django.contrib.auth.models import User
from datetime import datetime
from rest_framework import serializers
from main.models import List


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


##class UserSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only = True)
    #username = serializers.CharField(max_length = 300)
    #email = serializers.EmailField()
    #is_staff = serializers.BooleanField()
    #class Meta:
       # model = User
        #fields = ('id', 'username', 'email', )

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    tit_bl = serializers.CharField(max_length=200)
    text_bl = serializers.CharField(max_length=200)
    createted_at = serializers.DateTimeField(initial=datetime.now)
    author = UserSerializer(read_only = True)

    def create(self, validated_data):
        blog = List(**validated_data)
        blog.owner = User.objects.first()
        blog.save()
        return blog

    def update(self, instance, validated_data):
        instance.item = validated_data.get('item', instance.item)
        instance.save()
        return instance

class ListModelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = List
        fields = ['id', 'tit_bl', 'author']


