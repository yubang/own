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


class TimeBottleModel(models.Model):
    "时光瓶类"
    uid = models.IntegerField()
    content = models.CharField(max_length=255)
    targetTime = models.DateField()
    createTime = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        db_table = "own_time_bottle"


class PaperModel(models.Model):
    "纸条类"
    uid = models.IntegerField()
    content = models.CharField(max_length=255)
    status = models.IntegerField()
    createTime = models.DateTimeField()

    class Meta:
        db_table = "own_paper"
