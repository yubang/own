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


class DiaryModel(models.Model):
    uid = models.IntegerField()
    picUrl = models.CharField(max_length=200)
    content = models.CharField(max_length=255)
    pushTime = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        db_table = "own_diary"