# coding:UTF-8

from django.db import models


class AccountModel(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    halt = models.CharField(max_length=32)
    registerTime = models.DateTimeField()
    loginTime = models.DateTimeField()

    class Meta:
        db_table = "own_account"