from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import viewsets

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
