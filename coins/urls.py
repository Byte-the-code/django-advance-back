from django.urls import path

from coins.views import wallets_view, coin_details_view, portfolio, generate_data, card_delete


urlpatterns = [
    path('details/<int:pk>/', coin_details_view, name='coin_details'),
    path('wallets/', wallets_view, name='wallets'),
    path('portfolio/', portfolio, name='portfolio'),
    path('generate-data/', generate_data, name='generate_data'),
    path('card/delete/<int:pk>/', card_delete, name='delete_card'),
]