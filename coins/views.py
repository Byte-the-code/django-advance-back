import json
import random

from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse

from coins.utils import generate_transactions, get_details_graph_data
from coins.models import Card, Coin
from coins.forms import CardForm


def generate_data(request):
    generate_transactions()
    return HttpResponse('Data generated')

@login_required
def wallets_view(request):
    if request.method == 'GET':
        context = {
            'cards': Card.objects.filter(user=request.user)
        }
        return render(request, 'coins/wallets.html', context=context)
    
    elif request.method == 'POST':

        data = request.POST.copy()
        data['valid_date'] = datetime.strptime(request.POST['valid_date'], '%m/%y').date()

        form = CardForm(data)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.balance = random.randint(5000, 30000)
            card.save()
            return redirect('wallets')
        else:
            context = {
                'cards': Card.objects.filter(user=request.user),
                'errors': form.errors,
            }
            return render(request, 'coins/wallets.html', context=context)
        
@login_required
def card_delete(request, pk):
    card = Card.objects.get(pk=pk)
    if card.user != request.user:
        return redirect('wallets')
    card.delete()
    return redirect('wallets')

@login_required
def portfolio(request):
    coins = Coin.objects.all()
    for coin in coins:
        coin.user_amount = round(coin.user.filter(user=request.user).first().amount * coin.get_last_day_price(), 2)
    context = {
        'coins': coins
    }
    return render(request, 'coins/portfolio.html', context=context)

@login_required
def coin_details_view(request, pk):
    coin = get_object_or_404(Coin, pk=pk)
    context ={
        'coin': coin,
        'graph_data': json.dumps(get_details_graph_data(coin)),
    }
    return render(request, 'coins/coin_details.html', context=context)