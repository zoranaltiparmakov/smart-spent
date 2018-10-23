from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    LANG_CHOICES = (('Slovenian', 'Slovenian'), ('English', 'English'))
    language = models.CharField(choices=LANG_CHOICES, max_length=30, default='English')


class UserSettings(models.Model):
    language = models.ForeignKey(Language, on_delete=None, default=1)
    TRUE_FALSE_CHOICES = ((True, 'Yes'), (False, 'No'))
    enabled_notifications = models.BooleanField(choices=TRUE_FALSE_CHOICES, default=True)
    enabled_location = models.BooleanField(choices=TRUE_FALSE_CHOICES, default=True)


class Locations(models.Model):
    date = models.DateTimeField()
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)


class Transactions(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    date = models.DateTimeField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    settings = models.OneToOneField(UserSettings, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True)
    transactions = models.ForeignKey(Transactions, on_delete=models.CASCADE, null=True)
    points = models.IntegerField(default=0)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)
    postal_code = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    avatar = models.ImageField(upload_to='avatars/', blank=True, default='avatars/avatar.png')
