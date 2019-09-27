from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import viewsets, permissions
from todo.models import Todo

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        queryset = self.request.user.todo.all()

        is_done = self.request.query_params.get('done', None)
        
        if is_done is not None:
            queryset = queryset.filter(is_done=is_done)
        return queryset


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
