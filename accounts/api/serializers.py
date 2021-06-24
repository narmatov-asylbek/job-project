from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'password',
            'user_permissions',
            'is_superuser',
            'is_active',
            'is_staff',
            'last_login',
            'groups',
            'date_joined'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True,
                                      style={'input_type': 'password'}, label='Повторите пароль')

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'password2',
        )

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        password2 = validated_data['password2']

        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Пользователь с таким email уже существует"})
        if password != password2:
            raise serializers.ValidationError({"password2": "Пароли должны совпадать"})

        user = User(email=email)
        user.set_password(password)
        user.save()
        return user
