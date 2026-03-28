from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    tenant = serializers.CharField()
    user = serializers.CharField()
    role = serializers.CharField()

