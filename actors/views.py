from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import ActorModel, Nationality
from actors.serializers import ActorSerializers, NationalitySerializer
from app.permissions import GlobalPermissionClass


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializers


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializers


class NationalityListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Nationality.objects.all().order_by('name')
    serializer_class = NationalitySerializer


class NationalityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer