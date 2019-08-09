from .models import Post
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .serializers import SocCreateSerializers, SocListSerializers, SocDetailSerializers


class SocCreateView(generics.CreateAPIView):
    serializer_class = SocCreateSerializers


class SocListView(generics.ListAPIView):
    serializer_class = SocListSerializers
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, )


class SocDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = SocDetailSerializers
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, )

    def patch(self, request, *args, **kwargs):
       return self.update(request, *args, **kwargs)
