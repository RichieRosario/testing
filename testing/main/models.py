from django.db import models
from tinymce.widgets import TinyMCE
from tinymce import HTMLField

class JohnTest(models.Model):
	title = models.CharField(default='Hello', max_length=200)
	article_title = models.CharField(default='0000000', max_length=200)
	article_content =  HTMLField('Content')
	

	def __str__(self):
		return self.title
