from django.db import models
from django.urls import reverse
# Create your models here.

class Message(models.Model):
	name = models.CharField(max_length=60)
	email = models.EmailField(unique=True)
	message = models.TextField()


	def __str__(self):
		return self.name