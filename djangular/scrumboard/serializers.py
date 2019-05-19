from rest_framework import serializers

from .models import List, Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card


class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)

    class Meta:
        model = List




