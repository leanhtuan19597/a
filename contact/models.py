from django.db import models

# Create your models here.
class contactForm(models.Model):
	username = models.CharField(max_length = 25)
	email = models.CharField(max_length = 30)
	body = models.CharField(max_length = 500)

	def __str__(self):
		return self.username
		