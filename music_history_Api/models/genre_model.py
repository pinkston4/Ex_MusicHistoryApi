from django.db import models

class Genre(models.Model):
	"""
	Genre will only hold the name of the genre.
	__str__ method returns string representation of the genre name.
	Ordered on name
	"""
	name = models.CharField(max_length=100, blank=True, default='')

	def __str__	(self):
		return self.name

	class Meta:
		ordering = ('name',)
