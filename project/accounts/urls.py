from django.urls import path
from . import views


urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    # Later will be provided.
    path('end_points/', views.test_view, name='end_points'),
    path('login/', views.UserTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]
