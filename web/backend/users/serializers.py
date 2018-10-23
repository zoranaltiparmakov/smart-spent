from rest_framework import serializers, status
from rest_framework.response import Response

from users.models import User, Profile, UserSettings, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class UserSettingsSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(required=True)

    class Meta:
        model = UserSettings
        fields = '__all__'

    def update(self, instance, validated_data):
        new_language = validated_data['language']['language']
        language = Language.objects.get(language=new_language)
        instance.language = language
        instance.enabled_notifications = validated_data['enabled_notifications']
        instance.enabled_location = validated_data['enabled_location']
        instance.save()

        return Response(status=status.HTTP_201_CREATED)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    settings = UserSettingsSerializer(required=True)

    class Meta:
        model = Profile
        fields = '__all__'
