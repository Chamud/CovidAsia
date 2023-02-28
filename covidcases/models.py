from django.db import models

# Create your models here.

class countryCases(models.Model):
	country=models.CharField(max_length=100)
	confirmed=models.IntegerField()
	recovered=models.IntegerField()
	deaths=models.IntegerField()
	updated=models.CharField(max_length=100)
