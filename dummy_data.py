from blockchain.models import Shopper
from blockchain.test_factories import BlockFactory
import random

jack_ma = Shopper(name='Jack Ma', phone='09111222333', public_key='1MZ36MjvZSpGPsq7nKbCPoGDWrrD2wPvyoT2DC')
jack_ma.save(password='1234qwer')
BlockFactory(title='dell-inspiron', seller=jack_ma, price=random.randrange(100, 1000, 100))
BlockFactory(title='dell-latitude', seller=jack_ma, price=random.randrange(100, 1000, 100))
BlockFactory(title='ipad', seller=jack_ma, price=random.randrange(100, 1000, 100))
BlockFactory(title='ipad-pro', seller=jack_ma, price=random.randrange(100, 1000, 100))
BlockFactory(title='iphone-5s', seller=jack_ma, price=random.randrange(100, 1000, 100))
BlockFactory(title='iphone-6s', seller=jack_ma, price=random.randrange(100, 1000, 100))
BlockFactory(title='macbook-2016', seller=jack_ma, price=random.randrange(100, 1000, 100))
BlockFactory(title='msi1', seller=jack_ma, price=random.randrange(100, 1000, 100))
BlockFactory(title='note-5', seller=jack_ma, price=random.randrange(100, 1000, 100))
