from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mhp(models.Model):
    PAYMENT_CHOICES = [
        ('upi', 'UPI'),
        ('cod', 'Cash on Delivery'),
        ('card', 'Card Payment'),
        ('paypal', 'pay-pal'),
    ]

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.BigIntegerField()
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)

    def __str__(self):
        return self.name
