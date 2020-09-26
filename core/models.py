from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name= "user_profile", on_delete = models.CASCADE)

@receiver(post_save, sender=User, dispatch_uid="update_stock_count")
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    UserProfile(user=instance)

class Location(models.Model):

    latitude = models.DecimalField(max_digits=22, decimal_places=16, help_text="latitude")
    longitude = models.DecimalField(max_digits=22, decimal_places=16, help_text="longitude")
    location_set = models.ForeignKey("LocationSet", related_name="locations", on_delete= models.PROTECT)

    create_date = models.DateTimeField(auto_now_add=True)


class LocationSet(models.Model):
    
    user_profile = models.ForeignKey(UserProfile , related_name= "location_sets", on_delete= models.PROTECT)
    create_date = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
