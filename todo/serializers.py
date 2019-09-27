from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Todo
        fields = '__all__'
