from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import viewsets, permissions

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    permission_classes = [permissions.IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
