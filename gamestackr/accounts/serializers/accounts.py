from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

Account = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'email', 'password', 'password_confirm')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('The password do not match')
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        account = Account.objects.create_user(**validated_data)
        return account


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        account = authenticate(**data)
        if account and account.is_active:
            return account
        raise serializers.ValidationError('Incorrect credentials or inactive user')
