from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from users.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.


class RegisterUser(CreateAPIView):
    serializer_class = UserSerializer


class GetUser(RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
