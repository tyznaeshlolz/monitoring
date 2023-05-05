from django.urls import path, include
from rest_framework import routers
from .views import OSUserViewSet, GateViewSet, VisitLogViewSet


router = routers.DefaultRouter()
router.register('users', OSUserViewSet)
router.register('gates', GateViewSet)
router.register('visits', VisitLogViewSet, basename='visits')

urlpatterns = [
    path('', include(router.urls)),
    path('register_visit/', VisitLogViewSet.as_view({'post': 'register_visit'}))
]
