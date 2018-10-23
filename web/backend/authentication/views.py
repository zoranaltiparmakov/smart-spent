from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.defaultfilters import lower
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import UserSettings, Profile
from users.serializers import ProfileSerializer, UserSerializer, UserSettingsSerializer


class ObtainAuthToken(APIView):
    serializer_class = AuthTokenSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        existingToken = Token.objects.filter(user=user)
        if existingToken:
            existingToken.delete()

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })


class LogoutView(APIView):

    def get(self, request):
        request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)


class RegistrationView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        if User.objects.filter(email=request.data['email']).exists():
            errors = {
                'errors': {
                    'email': 'Email already exists.'
                }
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        username = lower(request.data['first_name']) + lower(request.data['last_name'])
        user = User.objects.create(
            username=username,
            first_name=request.data['first_name'],
            # add lastname for the user only if it is a string, otherwise add empty string
            last_name=request.data['last_name'] if not request.data['last_name'] == "1" else "",
            email=request.data['email'],
        )
        # save hashed password value
        user.set_password(request.data['password'])
        user.save()

        settings = UserSettings.objects.create()
        settings.save()

        profile = Profile.objects.create(
            user=user,
            settings=settings,
        )
        profile.save()

        serialized = ProfileSerializer(profile)
        if serialized:
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
