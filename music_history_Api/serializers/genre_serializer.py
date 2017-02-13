from rest_framework import serializers
from music_history_Api.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):
	"""
	serializer for genre model
	"""
	class Meta:
		model = genre_model.Genre
		fields='__all__'