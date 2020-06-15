from django.db import models

class Post(models.Model):
	post_title = models.CharField(max_length=300)
	post_date = models.DateTimeField()
	post_image = models.ImageField(upload_to='blog_images/')
	post_text = models.TextField()

	def get_summary(self):
		return self.post_text[:70]