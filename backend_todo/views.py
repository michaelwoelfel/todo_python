from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.response import Response
from rest_framework import status

# Create your views here
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('date')
    serializer_class = TodoSerializer
    permission_classes = []  # Uncomment this if you want to enable authentication
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
