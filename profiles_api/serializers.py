from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing the POST functionslity of our APIView"""

    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

