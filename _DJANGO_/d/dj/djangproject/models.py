from django.db import models

class BlogPost(models.Model):
	title = models.CharField(max__length=200)
	content = models.TextField()
	pub_date = models.DateTimeField()