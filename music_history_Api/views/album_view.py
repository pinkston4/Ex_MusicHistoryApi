from rest_framework import viewsets
from music_history_Api.serializers import *
from music_history_Api.models import *

class AlbumViewSet(viewsets.ModelViewSet):

	queryset = album_model.Album.objects.all()
	serializer_class = album_serializer.AlbumSerializer