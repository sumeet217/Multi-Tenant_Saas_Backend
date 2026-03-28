from django.urls import path
from .views import DashboardView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import AdminOnlyView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin-only/", AdminOnlyView.as_view()),
    path("dashboard/", DashboardView.as_view()),
]