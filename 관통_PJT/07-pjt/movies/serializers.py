from rest_framework import serializers
from .models import Movie, Review, Actor

# 전체 배우 목록 제공
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', )


# 단일 배우 정보 제공
class ActorDetailSerializer(serializers.ModelSerializer):

    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies', )


# 전체 영화 목록 제공
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', )
        

# 전체 리뷰 목록 제공 
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content', )
        
        
# 단일 영화 정보 제공
class MovieDetailSerializer(serializers.ModelSerializer):

    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    actors = ActorNameSerializer(many=True, read_only=True)

    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


# 단일 리뷰 정보 제공 
class ReviewDetailSerializer(serializers.ModelSerializer):

    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', )

    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


# 리뷰 데이터 저장
class ReviewSerializer(serializers.ModelSerializer):

    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content', )
        read_only_fields = ('id', 'movie')