from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from netflix.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register("kino", KinoViewSet),
router.register("aktyor", AktyorViewSet)
router.register("comments", CommentViewSet),



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('get_token/', TokenObtainPairView.as_view()),
    path('token_yangila/', TokenRefreshView.as_view()),
]
