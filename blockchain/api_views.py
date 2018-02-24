from blockchain.serializers import BlockSerializer
from blockchain.models import Block
from rest_framework import viewsets, mixins


class BlockViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
