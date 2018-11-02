from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliation  = models.CharField(max_length=30, blank=True)
    linked_in    = models.URLField(max_length=256,blank=True)
    image        = models.ImageField(upload_to='images/', blank=True, null=True)
    orcid		 = models.CharField(max_length=19, blank=True)
    gender       = models.CharField(max_length= 10, blank=True)
    birth_date   = models.DateField(default=date.today, blank=True)
    about_me     = models.CharField(max_length=300, blank=True)
    tweet_ammount= models.IntegerField(default=10, blank=True, validators=[MinValueValidator(1), MaxValueValidator(20)])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
