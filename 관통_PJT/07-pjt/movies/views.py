from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, ActorDetailSerializer,MovieListSerializer, MovieDetailSerializer, ReviewListSerializer, ReviewDetailSerializer, ReviewSerializer

# 전체 배우 목록 제공
@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
    

# 단일 배우 정보 제공
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    if request.method == 'GET':
        serializer = ActorDetailSerializer(actor)
        return Response(serializer.data)


# 전체 영화 목록 제공    
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

# 단일 영화 정보 제공
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    

# 전체 리뷰 목록 제공
@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    

# 단일 리뷰 정보 제공
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response({"message": f"review {review_pk} is deleted."}, status=status.HTTP_204_NO_CONTENT)
    

# 리뷰 데이터 저장 
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
