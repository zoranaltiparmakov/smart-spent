from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import Profile, UserSettings
from users.models import User
from users.serializers import ProfileSerializer, UserSettingsSerializer
from rest_framework import generics


class UserList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        """
        :return: Data for user requesting it
        """
        return Profile.objects.filter(user=self.request.user)


class SpecificUserDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserSettingsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSettingsSerializer

    def get_object(self):
        return UserSettings.objects.first()