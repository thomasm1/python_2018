from django.db import models

# Create your models here.
'''  Django ORM -- 
class BlogPost(models.Model):
    title = models.CharField(max__length=200)
	content = models.TextField()
	pub_date = models.DateTimeField()

bp = BlogPost()
bp.title = "djdata"
bp.save()

BlogPost.objects.filter(title="djdata").all()
 
Querying Data
BlogPost.query.filter_by(title="djdata")
'''