from django.urls import path, include
from rest_framework import routers
from .views import OSUserViewSet, GateViewSet


router = routers.DefaultRouter()
router.register('users', OSUserViewSet)
router.register('gates', GateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
