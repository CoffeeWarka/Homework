from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.IntegerField()
    size = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)