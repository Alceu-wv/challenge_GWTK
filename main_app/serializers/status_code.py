import arrow
from rest_framework import serializers


class BadRequestSerializer(serializers.Serializer):
    """Bad Request."""

    field = serializers.ListField(child=serializers.CharField(default="Bad request"))


class NotAuthorizedSerializer(serializers.Serializer):
    """Status 401 Response."""

    detail = serializers.CharField(default="Not authorized")


class AuthenticationFailedSerializer(serializers.Serializer):
    """Status 403 Response."""

    detail = serializers.CharField(default="Authorization header not found")


class GatewayTimeoutSerializer(serializers.Serializer):
    """Status 504 Response."""

    detail = serializers.CharField(default="Gateway Timeout")


class HealthCheckResponseSerializer(serializers.Serializer):
    """Response Ok."""

    status = serializers.CharField(default="OK")
    time = serializers.CharField(default=arrow.utcnow().isoformat())
