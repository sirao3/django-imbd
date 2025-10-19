from django.urls import path
# from .views import movie_list, movie_detail
from .views import WatchListAV, MovieDetailAV, StreamPlatformAV, StreamPlatformDetailAV,ReviewList,ReviewCreate,ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(),name="streaming-platform"),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name="stream-detail"),

    path('<int:pk>/review/',ReviewList.as_view(), name = "review-list"),
    path('<int:pk>/review-create/',ReviewCreate.as_view(), name = "review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail")
]