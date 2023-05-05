from django.urls import path, include
from rest_framework import routers
from .views import OSUserViewSet


router = routers.DefaultRouter()
router.register(r'users', OSUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
