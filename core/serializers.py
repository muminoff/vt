from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = ('username', 'phone_number', 'joined_date', 'last_seen')
