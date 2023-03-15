from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from coins.utils import generate_transactions
from coins.models import Coin, Transaction

# Create your views here.
@login_required
def wallets_view(request):
    return render(request, 'coins/wallets.html')

@login_required
def coin_details_view(request):
    return render(request, 'coins/coin_details.html')

@login_required
def portfolio(request):
    return render(request, 'coins/portfolio.html')

def generate_data(request):
    print(generate_transactions())
    return HttpResponse('Data generated')

def get_five_days_data(request):
    context = {
        'data':[]
    }
    date_array = [Transaction.get_last_day()]
    for i in range(1, 5):
        date_array.append(date_array[0] -timedelta(days=i))
    context['dates'] = date_array

    count = 0
    for coin in Coin.objects.all():
        context['data'].append(
            {
            'name':coin.name,
            'data':coin.get_last_five_days_data()
            }
        )
    
    print(context)
    return HttpResponse('Data generated')