from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = User
        fields = ['id','first_name','last_name','username', 'email' ] 
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = ['id','title', 'description', 'date', 'author','time_passed' ] # User

