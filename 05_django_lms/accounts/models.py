from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=50)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', null=True, blank=True)

    class Meta:
        db_table = 'profiles'


# post_save, sender=User
# created: True->Create, False->Update
# instance: User
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created'):
        profile = Profile(user=kwargs.get('instance'))
        profile.save()
