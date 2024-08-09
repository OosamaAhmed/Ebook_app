from django.db import models

# Create your models here.
class EBooksModel(models.Model):

	title = models.CharField(max_length = 20)
	summary = models.TextField(max_length=150)
	pages = models.CharField(max_length=30)
	pdf = models.FileField(upload_to='pdfs/')
	author = models.CharField(max_length=80)
	category = models.CharField(max_length=50)
	author_id = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.title}"
 