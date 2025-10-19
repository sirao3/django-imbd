from rest_framework import serializers
from watchlist_app.models import WatchList,StreamingPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only = True)
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id','name']
        # exclude = ['active']
    
class StreamingPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only = True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="movie-detail")
    class Meta:
        model = StreamingPlatform
        fields = '__all__'

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def delete(self, instance):
#         instance.delete()