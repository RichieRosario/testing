from django.db import models
from tinymce.widgets import TinyMCE

class JohnTest(models.Model):
	title = models.CharField(max_length=200)


	def __str__(self):
		return self.title