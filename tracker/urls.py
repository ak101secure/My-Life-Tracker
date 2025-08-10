from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, WorkSessionViewSet, FuturePlanViewSet, CompetitiveTaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')
router.register('worksessions', WorkSessionViewSet, basename='worksessions')
router.register('futureplans', FuturePlanViewSet, basename='futureplans')
router.register('competitivetasks', CompetitiveTaskViewSet, basename='competitivetasks')

urlpatterns = [
    path('', include(router.urls)),
]
