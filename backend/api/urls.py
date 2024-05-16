from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FollowViewSet, TagViewSet, IngredientViewSet, RecipeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'follows', FollowViewSet)
router.register(r'tags', TagViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
