from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import ActorModel
from actors.serializers import ActorSerializers
from app.permissions import GlobalPermissionClass


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializers


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializers
