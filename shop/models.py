from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

User = get_user_model()


class Balance(models.Model):
    value = models.PositiveIntegerField(
        verbose_name='Баланс',
        default=0
    )
    user = models.OneToOneField(
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='balance',
        to=User
    )

    def balance_minus(self, value):
        self.value -= value
        return self.save()
