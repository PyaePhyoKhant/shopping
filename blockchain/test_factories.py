import factory
from blockchain.models import Shopper, Block, TO_SELL
import random


class ShopperFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shopper

    name = factory.Faker('name')
    phone = '09' + ''.join([random.choice('0123456789') for _ in range(9)])


class BlockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Block

    title = random.choice(['bag', 'cat', 'dog', 'computer', 'phone'])
    price = random.randrange(1000, 100000, 100)
    seller = factory.SubFactory(ShopperFactory)
    buyer = factory.SubFactory(ShopperFactory)
    status = TO_SELL
