from django import forms

from coins.models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['card_name', 'card_holder', 'card_number', 'bank_name', 'valid_date', 'color']