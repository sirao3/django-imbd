from django.urls import path
# from .views import movie_list, movie_detail
from .views import WatchListAV, MovieDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),
    path('stream', StreamPlatformAV.as_view(),name="streaming-platform"),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name="stream-detail")
]