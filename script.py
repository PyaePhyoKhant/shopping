from blockchain.test_factories import BlockFactory
from django.contrib.auth.models import User

BlockFactory()
BlockFactory()
BlockFactory()
BlockFactory()
User.objects.create_user('user1', 'user1@gmail.com', '1234qwer')
User.objects.create_user('user2', 'user2@gmail.com', '1234qwer')
