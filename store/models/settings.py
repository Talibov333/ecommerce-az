from django.db import models
import datetime


class HomePageSetting(models.Model):
    pagetitle = models.CharField(max_length=60,blank=True)
    navbar = models.CharField(max_length=100,blank=True)
    navhome = models.CharField(max_length=60,blank=True)
    navcart = models.CharField(max_length=60,blank=True)
    navreg = models.CharField(max_length=60,blank=True)
    navlogin = models.CharField(max_length=60,blank=True)
    navlogout = models.CharField(max_length=60,blank=True)
    navaccount = models.CharField(max_length=60,blank=True)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.date
