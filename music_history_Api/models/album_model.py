from django.db import models
from . import song_model
from . import artist_model
from . import genre_model

class Album(models.Model):
	"""
	Class Album will contain album name, release date, artist, songs, and genre.
	__str__ method returns string representation of name
	odered by name
	"""
	name = models.CharField(max_length=100, blank=True, default='')
	release_date = models.DateField(auto_now_add=False)
	artist = models.ForeignKey(artist_model.Artist, related_name='artist')
	songs = models.ManyToManyField(song_model.Song)
	genre = models.ManyToManyField(genre_model.Genre)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)