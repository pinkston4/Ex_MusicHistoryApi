from rest_framework import viewsets
from music_history_Api.serializers import *
from music_history_Api.models import *

class SongViewSet(viewsets.ModelViewSet):

	queryset = song_model.Song.objects.all()
	serializer_class = song_serializer.SongSerializer