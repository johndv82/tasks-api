from rest_framework import viewsets
from .serializer import TaskSerializerr
from .models import Task

# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializerr
    queryset = Task.objects.all()