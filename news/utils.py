import random

from news.models import News



def get_random_news():
    all_news = News.objects.all()
    selected_news = random.choices(all_news, k = 4)
    return (selected_news[0], selected_news[1:])