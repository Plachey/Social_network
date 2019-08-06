from rest_framework import generics
from .serializers import UserSerializer
from . import models


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer
