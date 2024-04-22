import base64
import hashlib

from rest_framework import serializers
from shortener.models import URL
from shortener.queries import check_url_exists


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = URL
        fields = ['original_url', 'short_url']

    def create(self, validated_data):
        # Generate short URL
        original_url = validated_data['original_url']
        hash_object = hashlib.sha256(original_url.encode())
        hash_hex = hash_object.hexdigest()
        short_url = base64.urlsafe_b64encode(hash_hex.encode()).decode()[:8]  # Adjust length as needed
        if check_url_exists(short_url):
            raise serializers.ValidationError("url already exists")
        return URL.objects.create(**validated_data, short_url=short_url)
