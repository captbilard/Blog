from django.db import models
from django.utils import timezone 


# Create your models here.
#The view for the author to make post on the blog
class Author(models.Model):
	author_name  = models.CharField(max_length=100)
	display_name = models.CharField(max_length=30)
	email_address = models.EmailField()
	date_Joined = models.DateTimeField(default=timezone.now, editable=False)

	def __str__(self):
		return self.display_name

class PostView(models.Model):
	post_title = models.CharField(max_length = 100)
	post = models.TextField()
	image_check = models.BooleanField(default=False)
	image_post =  models.ImageField(upload_to = 'media/')
	date_posted = models.DateTimeField(default = timezone.now, editable = True)

	def __str__(self):
		return self.post_title

class User(models.Model):
	name = models.CharField(max_length=90)
	user_name = models.CharField(max_length=80)
	email_address = models.EmailField()

	def __str__(self):
		return self.user_name


