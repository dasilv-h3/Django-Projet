from django.shortcuts import render
from django.db.models import Q
from .models import Film, Actor
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def films(request):
    query = request.GET.get('q', '')
    if query:
        films = Film.objects.filter(title__icontains=query)
    else:
        films = Film.objects.all()
        
    context = {'films': films, 'query': query}
    return render(request, 'films.html', context)

def actors(request):
    query = request.GET.get('q', '')
    if query:
        actors = Actor.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    else:
        actors = Actor.objects.all()
    context = {'actors': actors, 'query': query}
    return render(request, 'actors.html', {'actors': actors, 'query': query})

def film_detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    actors = film.actors.all()
    print("ACTORS",actors)
    context = {
        "film": film,
        "actors": actors
    }
    return render(request, 'film_detail.html', context)