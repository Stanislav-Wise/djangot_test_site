from django.shortcuts import render
from .models import Movie
from .forms import MovieFilterForm

def movie_list(request):
    # Инициализация формы
    form = MovieFilterForm(request.GET or None)

    # Базовый QuerySet
    movies = Movie.objects.all()

    # Применение фильтров
    if form.is_valid():
        title = form.cleaned_data.get('title')
        genre = form.cleaned_data.get('genre')
        min_rating = form.cleaned_data.get('min_rating')
        max_rating = form.cleaned_data.get('max_rating')
        release_date_from = form.cleaned_data.get('release_date_from')
        release_date_to = form.cleaned_data.get('release_date_to')

        if title:
            movies = movies.filter(title__icontains=title)
        if genre:
            movies = movies.filter(genre__icontains=genre)
        if min_rating:
            movies = movies.filter(rating__gte=min_rating)
        if max_rating:
            movies = movies.filter(rating__lte=max_rating)
        if release_date_from:
            movies = movies.filter(release_date__gte=release_date_from)
        if release_date_to:
            movies = movies.filter(release_date__lte=release_date_to)

    # Отправка данных в шаблон
    context = {
        'form': form,
        'movies': movies,
    }
    return render(request, 'movie_app/movie_list.html', context)
