
from django.conf.urls import url, include
from rest_framework import routers
from music_history_Api.views import *

# Create a router, using DefaultRouter
# Register each ViewSet with it.
router = routers.DefaultRouter()
router.register(r'artists', artist_view.ArtistViewSet)
router.register(r'songs', song_view.SongViewSet)
router.register(r'albums', album_view.AlbumViewSet)
router.register(r'genres', genre_view.GenreViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
