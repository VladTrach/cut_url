from rest_framework import serializers


class ShortcutSerializer(serializers.Serializer):
    shortcut = serializers.CharField(required=True)
