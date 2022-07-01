from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
