from rest_framework import serializers
from music_history_Api.models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
	"""
	serializer for song model
	"""
	class Meta:
		model = song_model.Song
		fields='__all__'