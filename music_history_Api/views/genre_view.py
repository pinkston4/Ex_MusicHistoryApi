from rest_framework import viewsets
from music_history_Api.serializers import *
from music_history_Api.models import *

class GenreViewSet(viewsets.ModelViewSet):

		queryset = genre_model.Genre.objects.all()
		serializer_class = genre_serializer.GenreSerializer