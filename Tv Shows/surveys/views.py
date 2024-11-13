from django.shortcuts import render, redirect, get_object_or_404
from .models import Show
from django.utils import timezone
from django.contrib import messages


def index(request):
    return redirect('all_shows')

def all_shows(request):
    shows = Show.objects.all()
    return render(request, 'all_shows.html', {'shows': shows})

def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    if request.method == 'POST':
        postData = {
            'title': request.POST.get('title'),
            'network': request.POST.get('network'),
            'release_date': request.POST.get('release_date'),
            'description': request.POST.get('description')
        }
        

        errors = Show.objects.basic_validator(postData)
        
        if errors:
            return render(request, 'new_show.html', {'errors': errors, 'postData': postData})
        else:
            Show.objects.create(**postData)
            return redirect('/shows')  
    
    return render(request, 'new_show.html') 

def success_page(request):
    return render(request, 'all_shows.html')  

def show_details(request, id):
    show = get_object_or_404(Show, id=id)
    return render(request, 'show_details.html', {'show': show})

def edit_show(request, id):
    show = get_object_or_404(Show, id=id)
    return render(request, 'edit_show.html', {'show': show})


def update_show(request, id):
    show = get_object_or_404(Show, id=id)
    
    if request.method == 'POST':
        postData = {
            'title': request.POST.get('title'),
            'network': request.POST.get('network'),
            'release_date': request.POST.get('release_date'),
            'description': request.POST.get('description')
        }

        errors = Show.objects.basic_validator(postData)
        
        if errors:
            return render(request, 'edit_show.html', {'errors': errors, 'postData': postData, 'show': show})
        else:
            show.title = postData['title']
            show.network = postData['network']
            show.release_date = postData['release_date']
            show.description = postData['description']
            show.last_updated = timezone.now()
            show.save()
            return redirect('show_details', id=show.id)


def delete_show(request, id):
    show = get_object_or_404(Show, id=id)
    show.delete()
    return redirect('all_shows')


