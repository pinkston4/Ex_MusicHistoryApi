from django.db import models
from . import artist_model
from . import genre_model

class Song(models.Model):
	"""
	Class song will contain song name, release date, artist, genre
	method __str__ returns string of name
	odered by name
	"""
	name = models.CharField(max_length=100, blank=True, default='')
	release_date = models.DateField(auto_now_add=False)
	artist = models.ManyToManyField(artist_model.Artist)
	genre = models.ForeignKey(genre_model.Genre, related_name='genre')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)