from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import loader, RequestContext
from django.template.context_processors import csrf
from django import forms
from .models import Movie, Director, Genre
from Movie.forms import MovieForm, DirectorForm, GenreForm


# Create your views here.

def index(request):
    return render_to_response('Movie/index.html')


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'Movie/movie.html', {'movie': movie})


def director_detail(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    movies = Movie.objects.all().filter(director_id=director_id)
    return render(request, 'Movie/director.html', {'director': director, 'movies': movies})


def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    return render(request, 'Movie/genre.html', {'genre': genre})


def list_all_movies(request):
    all_movies = Movie.objects.all().order_by('name')
    context = {'all_movies': all_movies}
    return render(request, 'Movie/movies.html', context)


def list_all_directors(request):
    all_directors = Director.objects.all().order_by('name')
    context = {'all_directors': all_directors}
    return render(request, 'Movie/directors.html', context)


def list_all_genres(request):
    all_genres = Genre.objects.all().order_by('name')
    context = {'all_genres': all_genres}
    return render(request, 'Movie/genres.html', context)


def add_movie(request):
    success = False
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            return render(request, 'Movie/add_movie.html', {'form': form, 'success': success})
    else:
        form = MovieForm()
    return render(request, 'Movie/add_movie.html', {'form': form, 'success': success})


def add_director(request):
    success = False
    if request.method == 'POST':
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            return render(request, 'Movie/add_director.html', {'form': form, 'success': success})
    else:
        form = DirectorForm()
    return render(request, 'Movie/add_director.html', {'form': form, 'success': success})


def add_genre(request):
    success = False
    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            return render(request, 'Movie/add_genre.html', {'form': form, 'success': success})
    else:
        form = GenreForm()
    return render(request, 'Movie/add_genre.html', {'form': form, 'success': success})
