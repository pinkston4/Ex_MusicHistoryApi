from rest_framework import serializers
from music_history_Api.models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	"""
	serializer for album model
	"""
	class Meta:
		model = album_model.Album
		fields='__all__'