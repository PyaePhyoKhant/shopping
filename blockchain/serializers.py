from rest_framework import serializers
from blockchain.models import Block


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('id', 'title', 'created_at', 'price', 'seller', 'buyer', 'status')
