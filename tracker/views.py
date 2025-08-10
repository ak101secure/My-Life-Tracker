from rest_framework import viewsets, permissions
from .models import Task, WorkSession, FuturePlan, CompetitiveTask
from .serializers import TaskSerializer, WorkSessionSerializer, FuturePlanSerializer, CompetitiveTaskSerializer

class TaskViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorkSessionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WorkSessionSerializer

    def get_queryset(self):
        return WorkSession.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FuturePlanViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FuturePlanSerializer

    def get_queryset(self):
        return FuturePlan.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CompetitiveTaskViewSet(viewsets.ModelViewSet):
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CompetitiveTaskSerializer
    def get_queryset(self):
        return CompetitiveTask.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
