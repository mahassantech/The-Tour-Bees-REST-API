from rest_framework import serializers
from .models import TourPackageModel


class TourPackageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TourPackageModel
        fields = "__all__"
        read_only_fields = ["created_by", "created_at"]
