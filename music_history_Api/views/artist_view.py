from rest_framework import viewsets
from music_history_Api.serializers import *
from music_history_Api.models import *

class ArtistViewSet(viewsets.ModelViewSet):

	queryset = artist_model.Artist.objects.all()
	serializer_class = artist_serializer.ArtistSerializer