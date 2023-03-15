from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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