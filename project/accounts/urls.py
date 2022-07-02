from django.urls import path
from . import views


urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    # Later will be provided.
    path('end_points/', views.test_view, name='end_points'),
    path('phone_pass_get_token/', views.phone_pass_get_token,name='phone_pass_get_token'),
    path('login/', views.UserTokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('login2/', MyView.as_view(), name='login2'),
]

