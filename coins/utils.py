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

def get_five_days_data():
    context = {
        'data':[]
    }
    date_array = [Transaction.get_last_day()]
    for i in range(1, 5):
        date_array.append((date_array[0] - timedelta(days=i)).strftime('%d/%m'))
    date_array[0] = date_array[0].strftime('%d/%m')
    date_array.reverse()
    context['dates'] = date_array

    for coin in Coin.objects.all():
        context['data'].append(
            {
            'name':coin.name,
            'data':coin.get_last_five_days_data()
            }
        )
    
    return context

def get_details_graph_data(coin):
    context = []
    last_day =Transaction.get_last_day()
    for i in range(1, 11):
        context.append({last_day.strftime('%d/%m'):round(coin.get_price_by_date(last_day), 2)})
        last_day -= timedelta(days=1)
    context.reverse()
    return context

def get_recent_transactions():
    since_day = Transaction.get_last_day() - timedelta(days=2)
    return random.choices(Transaction.objects.filter(date__gte=since_day), k=6) #date >= since_day (Greater than or equal to)

