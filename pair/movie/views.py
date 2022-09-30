from django.dispatch import receiver
from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie' : movie,
    }
    return render(request, 'movie/index.html', context)

def new(request):
    
    return render(request, 'movie/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    Movie.objects.create(title=title, content=content)
    context = {
        'title' : title,
        'content' : content,
    }
    return render(request, 'posts/create.html', context)

    # return render(request, 'posts/create.html', context)
    #return redirect('movie:index')

def delete(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie:index')

def detail(request, pk):
    movies = Movie.objects.get(pk = pk)
    context = {
        'movies' : movies,
    }
    return render(request, 'movie/detail.html',context)

def edit(request, pk):
  movies = Movie.objects.get(pk = pk)
  context = {
    "movies": movies,
  }
  
  return render(request, 'movie/edit.html', context)
    
def update(request,pk):
    movies = Movie.objects.get(pk = pk)
    
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    movies.title = title
    movies.content = content
    movies.save()
       
    return redirect('movie:detail', movies.pk)