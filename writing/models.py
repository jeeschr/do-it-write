from django.db import models

# Create your models here.

class Review(models.Model):
	text=models.TextField()
	datetime=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class Text(models.Model):
	text=models.TextField()
	datetime=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class Character(models.Model):
	text=models.TextField()
	datetime=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class Event(models.Model):
	text=models.TextField()
	datetime=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text						