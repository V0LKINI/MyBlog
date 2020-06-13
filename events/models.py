from django.db import models

class event(models.Model):
	event_image = models.ImageField(upload_to='event_images/')
	event_text = models.CharField(max_length=300)