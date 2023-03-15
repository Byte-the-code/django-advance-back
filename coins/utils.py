import random

from datetime import timedelta

from django.utils import timezone

from coins.models import Transaction, Coin

def generate_price():
    return random.randint(10000, 30000) * random.random()

def generate_amount():
    return random.randint(1, 200) * random.random()

def generate_transaction_type():
    return random.choice(['buy', 'sell'])

def generate_transactions():
    transactions_to_create = []
    for coin in Coin.objects.all():
        today = timezone.now()
        for i in range(1, 31): #For each day
            for j in range(1,31):
                new_transaction = Transaction(
                    coin = coin,
                    price = generate_price(),
                    amount = generate_amount(),
                    date = today,
                    transaction_type = generate_transaction_type(),
                )
                transactions_to_create.append(new_transaction)
            today -= timedelta(days=1)
    Transaction.objects.bulk_create(transactions_to_create)

