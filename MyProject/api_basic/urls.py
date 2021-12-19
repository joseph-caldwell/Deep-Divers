from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')


urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
 
]