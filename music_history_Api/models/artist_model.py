from django.db import models
from . import genre_model

class Artist(models.Model):
	"""
	Class Artist will hold the artist name, genre, and bio.
	__str__ returns a string of the artist name
	ordered by name
	"""
	name = models.CharField(max_length=100, blank=True, default='')
	bio = models.CharField(max_length=400, default='')
	genre = models.ManyToManyField(genre_model.Genre)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)