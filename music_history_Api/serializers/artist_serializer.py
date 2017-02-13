from rest_framework import serializers
from music_history_Api.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	"""
	serializer for artist model
	"""
	class Meta:
		model = artist_model.Artist
		fields='__all__'