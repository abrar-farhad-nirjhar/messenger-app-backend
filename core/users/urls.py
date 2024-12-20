from rest_framework.authtoken import views
from django.urls import path
from users.views import (
    RegisterUser,
    GetUser,
)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('register/', RegisterUser.as_view()),
    path('get-current-user/', GetUser.as_view()),
]
