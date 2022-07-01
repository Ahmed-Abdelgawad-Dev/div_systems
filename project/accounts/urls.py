from django.urls import path
from . import views


urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path('test_view/', views.test_view, name='test_view')
]
