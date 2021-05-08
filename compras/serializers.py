from rest_framework import serializers

from .models import ComprasItem


class ComprasItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComprasItem
        fields = '__all__'