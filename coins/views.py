from django.shortcuts import render

# Create your views here.
def wallets_view(request):
    return render(request, 'coins/wallets.html')

def coin_details_view(request):
    return render(request, 'coins/coin_details.html')

def portfolio(request):
    return render(request, 'coins/portfolio.html')