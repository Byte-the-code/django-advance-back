from django.contrib import admin

from users.models import UserProfile, CoinAmount

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(CoinAmount)
class CoinAmountAdmin(admin.ModelAdmin):
    list_display = ['user', 'coin', 'amount']