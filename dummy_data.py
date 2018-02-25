from blockchain.models import Shopper
from blockchain.test_factories import BlockFactory
import random

ppk = Shopper.objects.get(name='Pyae Phyo Khant')
BlockFactory(title='dell-inspiron', seller=ppk, price=random.randrange(1000, 100000, 100))
BlockFactory(title='dell-latitude', seller=ppk, price=random.randrange(1000, 100000, 100))
BlockFactory(title='ipad', seller=ppk, price=random.randrange(1000, 100000, 100))
BlockFactory(title='ipad-pro', seller=ppk, price=random.randrange(1000, 100000, 100))
BlockFactory(title='iphone-5s', seller=ppk, price=random.randrange(1000, 100000, 100))
BlockFactory(title='iphone-6s', seller=ppk, price=random.randrange(1000, 100000, 100))
BlockFactory(title='macbook-2016', seller=ppk, price=random.randrange(1000, 100000, 100))
BlockFactory(title='msi1', seller=ppk, price=random.randrange(1000, 100000, 100))
BlockFactory(title='note-5', seller=ppk, price=random.randrange(1000, 100000, 100))
