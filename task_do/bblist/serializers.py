# -*- coding: utf-8 -*-
from rest_framework import serializers
from bblist.models import Task, IceCream
from .models import CustomUser


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class IceCreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(write_only=True)  # Поле для пароля
    password_2 = serializers.CharField(write_only=True)  # Поле для подтверждения пароля

    class Meta:
        model = CustomUser
        fields = (
            'username', 'password_1', 'password_2', 'first_name', 'last_name', 'email', 'is_active',
            'is_staff', 'is_superuser', 'bio', 'profile_picture', 'groups', 'user_permissions'
        )

    def create(self, validated_data):
        password_1 = validated_data.pop('password_1', None)
        password_2 = validated_data.pop('password_2', None)

        if password_1 != password_2:
            raise serializers.ValidationError("Пароль и подтверждение пароля не совпадают.")

        user = CustomUser(**validated_data)
        user.set_password(password_1)
        user.save()
        return user
