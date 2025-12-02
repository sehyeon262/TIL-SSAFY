import os
import json
import requests
from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_safe
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def fetch_director_data(name):

    headers = {
        "User-Agent": "MovieApp/1.0 (contact@example.com)" 
    }
    
    url = f"https://ko.wikipedia.org/api/rest_v1/page/summary/{name}"
    
    res = requests.get(url, headers=headers)
    
    if res.status_code == 200:
        data = res.json()
        return {
            "summary": data.get("extract"),
            "image_url": data.get("thumbnail", {}).get("source"),
        }
    
    return {}


def generate_director_info(name, wiki_summary):

    prompt = f"""
    감독 이름: {name}
    위키 요약: {wiki_summary}

    JSON 형태로 감독 소개와 대표작 목록을 만들어줘.
    {{
      "info": "감독에 대한 간단한 설명",
      "works": ["작품1", "작품2", "작품3"]
    }}
    """

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"info": content, "works": []}

@require_safe
def index(request):
    movies = Movie.objects.all()

    context = {
        'movies' : movies
    }

    return render(request, 'movies/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)

            if movie.director:
                wiki_data = fetch_director_data(movie.director)
                ai_data = generate_director_info(movie.director, wiki_data.get("summary", ""))

                movie.director_img_url = wiki_data.get("image_url")
                movie.director_info = ai_data.get("info")
                movie.director_works = ", ".join(ai_data.get("works", []))

            movie.save()  
            
            return redirect('movies:detail', movie.pk)
        
    else: 
        form = MovieForm()

    context = {
        'form' : form
    }

    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = CommentForm()
    comments = movie.comment_set.all()

    context = {
        'movie' : movie,
        'form' : form,
        'comments':comments,
    }

    return render(request, 'movies/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance = movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    
    else: 
        form = MovieForm(instance = movie)

    context = {
        'movie' : movie,
        'form' : form
    }

    return render(request, 'movies/update.html', context)

@require_http_methods(['POST'])
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()

    return redirect('movies:index')


@login_required
@require_http_methods(['POST'])
def comments_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.movie = movie
        comment.save()
        return redirect('movies:detail', movie.pk)
    
@require_http_methods(['POST'])
def comments_delete(request, comment_pk, movie_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)
    

