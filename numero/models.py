from django.db import models
from katysite.models import MainMenu


class NumeroMenu(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(null=False, unique=True)
    main_page = models.ForeignKey(MainMenu, on_delete=models.PROTECT)


class Celeb(models.Model):
    name = models.CharField(max_length=90)
    birthday = models.DateField()
    persid = models.IntegerField()


class CelebData(models.Model):
    celeb = models.OneToOneField(Celeb, on_delete=models.PROTECT, primary_key=True)
    profession = models.CharField(max_length=190)
    profile_url = models.URLField(max_length=255)
    photo_url = models.URLField(max_length=255)


class CalcMatrix(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    calc_date = models.DateField(unique=True)
    calc_result = models.JSONField()
