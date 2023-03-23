import random

from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from coins.utils import generate_transactions
from coins.models import Card
from coins.forms import CardForm

# Create your views here.
@login_required
def coin_details_view(request):
    return render(request, 'coins/coin_details.html')

@login_required
def portfolio(request):
    return render(request, 'coins/portfolio.html')

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