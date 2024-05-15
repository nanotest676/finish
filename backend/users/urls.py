from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FollowViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'follows', FollowViewSet)

urlpatterns = [
    path('users/', UserViewSet),
    path('auth/', include('djoser.urls.authtoken')),
]
