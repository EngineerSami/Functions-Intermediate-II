from django.shortcuts import render, redirect, get_object_or_404
from .models import Show
from django.utils import timezone

def index(request):
    return redirect('all_shows')

def all_shows(request):
    shows = Show.objects.all()
    return render(request, 'all_shows.html', {'shows': shows})

def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    if request.method == 'POST':
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        show = Show.objects.create(
            title=title, network=network, release_date=release_date, description=description
        )
        return redirect('show_details', id=show.id)

def show_details(request, id):
    show = get_object_or_404(Show, id=id)
    return render(request, 'show_details.html', {'show': show})

def edit_show(request, id):
    show = get_object_or_404(Show, id=id)
    return render(request, 'edit_show.html', {'show': show})

def update_show(request, id):
    if request.method == 'POST':
        show = get_object_or_404(Show, id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.last_updated = timezone.now()
        show.save()
        return redirect('show_details', id=show.id)

def delete_show(request, id):
    show = get_object_or_404(Show, id=id)
    show.delete()
    return redirect('all_shows')
