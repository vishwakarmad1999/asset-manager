from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class AuthenticateUser(models.Model):
	user 		= models.OneToOneField(User)
	is_verified = models.BooleanField(default = False)
	otp			= models.IntegerField(default = True, null = True)

	def __str__(self):
		return self.user.username

# def au_pre_save_receiver(sender, instance, *args, **kwargs):
# 	pass

# pre_save.connect(au_pre_save_receiver, sender = User)


def au_post_save_receiver(sender, instance, created, *args, **kwargs):
	if created:
		obj = AuthenticateUser(user = instance)
		obj.save()


post_save.connect(au_post_save_receiver, sender = User)