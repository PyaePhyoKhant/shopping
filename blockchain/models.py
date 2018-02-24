from django.db import models
from django.contrib.auth.models import User
import string
import random
import hashlib
from django.utils import timezone

TO_SELL = 'to sell'
SOLD = 'sold'


class Shopper(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    user = models.OneToOneField(User, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.user:
            email = str(self.name) + '@gmail.com'
            chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
            password = ''.join(random.choice(chars) for _ in range(8))
            self.user = User.objects.create_user(self.name, email, password)
        super(Shopper, self).save(*args, **kwargs)


def hash_block(block_instance):
    return hashlib.sha256(str(block_instance.id).encode('utf-8') +
                          str(block_instance.title).encode('utf-8') +
                          str(block_instance.created_at).encode('utf-8') +
                          str(block_instance.price).encode('utf-8') +
                          str(block_instance.seller).encode('utf-8') +
                          str(block_instance.status).encode('utf-8') +
                          str(block_instance.prev_id).encode('utf-8') +
                          str(block_instance.prev_hash).encode('utf-8')).digest()


class Block(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()
    seller = models.ForeignKey(Shopper, related_name='seller', blank=True, null=True)
    buyer = models.ForeignKey(Shopper, related_name='buyer', blank=True, null=True)

    status = models.CharField(max_length=100)
    prev_id = models.IntegerField(blank=True, null=True)
    prev_hash = models.BinaryField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if Block.objects.count() != 0:
            latest_block = Block.objects.latest('created_at')
            self.prev_hash = hash_block(latest_block)
        super(Block, self).save(*args, **kwargs)
