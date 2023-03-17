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
    generate_transactions()
    return HttpResponse('Data generated')

