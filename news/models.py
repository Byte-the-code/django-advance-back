from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url_to_news = models.CharField(max_length=255)
    url_to_image = models.CharField(max_length=255)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title