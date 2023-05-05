from rest_framework import serializers
from .models import OSUser


class OSUserSerializer(serializers.ModelSerializer):
    pass_number = serializers.SerializerMethodField(read_only=True)

    def get_pass_number(self, obj):
        return obj.login + obj.created_at.strftime('%Y%m%d')

    class Meta:
        model = OSUser
        fields = '__all__'
