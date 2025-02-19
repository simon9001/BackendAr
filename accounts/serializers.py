from rest_framework import serializers
from .models import User  # Ensure the correct import

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_student', 'is_lecturer', 'is_superuser', 'role']

    def get_role(self, obj):
        """Returns a string indicating the user's role"""
        if obj.is_superuser:
            return "admin"
        elif obj.is_student:
            return "student"
        elif obj.is_lecturer:
            return "lecturer"
        return "unknown"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_student', 'is_lecturer']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
