import random

from django.contrib.auth.models import User

from users.models import CoinAmount
from coins.models import Coin 

def generate_coin_amount():
    return round((random.randint(0, 50) * random.random())/10, 2)


def generate_user_coin_amount():
    for user in User.objects.all():
        for coin in Coin.objects.all():
            if not CoinAmount.objects.filter(user=user, coin=coin).exists():
                CoinAmount.objects.create(user=user, coin=coin, amount=generate_coin_amount())