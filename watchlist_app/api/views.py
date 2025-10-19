from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList,StreamingPlatform
from .serializers import WatchListSerializer,StreamingPlatformSerializer
from rest_framework import status

class StreamPlatformAV(APIView):
    def get(self, request):
        streamers = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(streamers,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            stream = StreamingPlatform.objects.get(pk=pk)
            serializer = StreamingPlatformSerializer(stream)
            return Response(serializer.data)
        except StreamingPlatform.DoesNotExist:
            return Response({"error": "Stream not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        stream = StreamingPlatform.objects.get(pk=pk)
        serializer = StreamingPlatformSerializer(stream,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        try:
            stream = StreamingPlatform.objects.get(pk=pk)
            stream.delete()
            return Response({"message": "Movie deleted successfully"})
        except StreamingPlatform.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class MovieDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            movie.delete()
            return Response({"message": "Movie deleted successfully"})
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        
# @api_view(['GET','POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):

#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
#         except Movie.DoesNotExist:
#             return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#             movie.delete()
#             return Response({"message": "Movie deleted successfully"})
#         except Movie.DoesNotExist:
#             return Response(status=status.HTTP_204_NO_CONTENT)