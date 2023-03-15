from datetime import timedelta

from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models import Avg
from django.db import models


class Card(models.Model):

    CHOICES = (
        ('purple', 'purple'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('orange', 'orange'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    card_name = models.CharField(max_length=40)
    card_holder = models.CharField(max_length=60)
    card_number = models.IntegerField(validators=[
                                                    MinValueValidator(4300000000000000), 
                                                    MaxValueValidator(4399999999999999)
                                                    ])
    bank_name = models.CharField(max_length=80)
    valid_date = models.DateField()
    color = models.CharField(max_length=6, choices=CHOICES, default='purple')

    def __str__(self):
        return self.card_name

class Coin(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to='coins')

    def __str__(self):
        return self.name
    
    def get_last_day(self):
        return self.transactions.all().order_by('-date').first().date.date()
    
    def get_average_transactions_by_date(self, date):
        return self.transactions.filter(date__date=date).aggregate(average = Avg('price'))
    
    def get_last_five_days_data(self):
        data = []
        last_day = self.get_last_day()
        for i in range(1, 6):
            data.append(self.get_average_transactions_by_date(last_day)['average'])
            last_day -= timedelta(days=1)
        return data

class Transaction(models.Model):

    CHOICE = (
        ('buy', 'buy'),
        ('sell', 'sell'),
    )

    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='transactions')
    price = models.FloatField()
    amount = models.FloatField()
    date = models.DateTimeField()
    transaction_type = models.CharField(max_length=4, choices=CHOICE)

    def __str__(self):
        return self.coin.name + ' ' + self.transaction_type
    
    @classmethod
    def get_last_day(cls):
        return cls.objects.all().order_by('-date').first().date.date()