from rest_framework import serializers
from .models import Task, WorkSession, FuturePlan, CompetitiveTask
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class WorkSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSession
        fields = '__all__'

class FuturePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuturePlan
        fields = '__all__'

class CompetitiveTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitiveTask
        fields = '__all__'
