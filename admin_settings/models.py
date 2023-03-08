from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'

class Language(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'