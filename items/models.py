from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Asset(models.Model):
	user 				= models.ForeignKey(User, on_delete = models.CASCADE)	
	asset_id			= models.CharField(max_length = 10, primary_key = True)
	plant				= models.CharField(max_length = 20, blank = True, null = True)
	location			= models.CharField(max_length = 20, blank = True, null = True)
	department			= models.CharField(max_length = 20, blank = True, null = True)
	username			= models.CharField(max_length = 50, blank = True, null = True)
	hostname			= models.CharField(max_length = 25, blank = True, null = True)
	email_id			= models.EmailField(blank = True, null = True)
	model 				= models.CharField(max_length = 30, blank = True, null = True)
	asset_code			= models.CharField(max_length = 15, blank = True, null = True)
	date_of_purchase	= models.DateField(blank = True, null = True)
	warranty_expiry 	= models.DateField(blank = True, null = True)
	configuration		= models.CharField(max_length = 40, blank = True, null = True)
	amount				= models.IntegerField(blank = True, null = True)
	operating_system	= models.CharField(max_length = 20, blank = True, null = True)

	ASSET_TYPE = (
			('Laptop', 'Laptop'),
			('Printer', 'Printer'),
			('Scanner', 'Scanner'),
			('Desktop', 'Desktop'),
			('Keyboard', 'Keyboard'),
			('Mouse', 'Mouse'),
			('Modem', 'Modem'),
			('Router', 'Router'),
			('Switch', 'Switch'),
			('Others', 'Others'),
		)
	category 			= models.CharField(max_length = 8, choices = ASSET_TYPE)


	def __str__(self):
		return self.asset_id


