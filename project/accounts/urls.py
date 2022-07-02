from django.urls import path
from . import views


urlpatterns = [
    path('task_one/', views.register_user),
    path('task_two/', views.UserTokenObtainPairView.as_view()),
    path('task_three/', views.phone_token_login),
]

