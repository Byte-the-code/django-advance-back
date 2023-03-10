import requests
from django.shortcuts import HttpResponse

from django_base.settings import NEWS_API_KEY

from news.models import News 


def fetch_news(request):
    response = requests.get(f'https://newsapi.org/v2/everything?q=bitcoin&apiKey={NEWS_API_KEY}')
    if response.status_code != 200:
        return HttpResponse(response.status_code)
    response = response.json()
    count = 0
    for article in response['articles']:
        if all([article['title'], 
                    article['description'], 
                    article['url'], 
                    article['urlToImage'], 
                    article['publishedAt']]):
            News.objects.create(
                title=article['title'],
                description=article['description'],
                url_to_news=article['url'],
                url_to_image=article['urlToImage'],
                published_at=article['publishedAt']
            )
            count += 1

    return HttpResponse('News fetched: ' + str(count))


