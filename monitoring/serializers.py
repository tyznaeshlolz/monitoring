from rest_framework import serializers
from .models import Gate, OSUser


class OSUserSerializer(serializers.ModelSerializer):
    pass_number = serializers.SerializerMethodField(read_only=True)

    def get_pass_number(self, obj):
        return obj.login + obj.created_at.strftime('%Y%m%d')

    class Meta:
        model = OSUser
        fields = '__all__'


class GateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gate
        fields = '__all__'
