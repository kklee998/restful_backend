from rest_framework import serializers
from django.contrib.auth.models import User
from todo.models import Todo


# User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    todo = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'todo')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        def create(self, validated_data):
            user = User.objects.create_user(
                validated_data['username'],
                validated_data['email'],
                validated_data['password']
                )
                
            return user
