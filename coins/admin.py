from django.contrib import admin

from coins.models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name',)