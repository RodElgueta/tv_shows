from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.db import IntegrityError

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return redirect("/shows")

def shows(request):
    context = {'shows' : Shows.objects.all()}
    return render(request, 'shows.html',context)

def new(request):
    context = {'networks' : Networks.objects.all()}
    return render (request, 'new.html',context)

def createshow(request):
    title = request.POST['title']
    desc = request.POST['desc']
    net = request.POST['network']
    release_date = request.POST['release_date']
    
    shows = Shows.objects.all()
    errors = Shows.objects.basic_valid(request.POST,shows)
    
    if len(errors) > 0:
        for key, error_msg in errors.items():
            messages.error(request, error_msg)
        return redirect('/shows/new')
    try:
        new_show = Shows.objects.create (title = title, desc = desc , network = Networks.objects.get(id=int(net)), release_date = release_date)
    except IntegrityError:
        messages.error(request,"This show alrready exist")
        return redirect('/shows/new')
        
    messages.success(request, f'Show {title} has been Created')
    return redirect(f"/shows/{new_show.id}")

def view(request,int):
    show = Shows.objects.get(id=int)
    
    context = {'show': show}

    return render(request, 'view.html',context)

def edit(request,int):
    show = Shows.objects.get(id=int)
    datestring = show.release_date.strftime("%Y-%m-%d")
    context = {'show': show,
                'networks':Networks.objects.all(),
                'datestring':datestring}

    

    return render(request, 'edit.html',context)

def editshow(request,show_id):
    show = Shows.objects.get(id=int(show_id))
    title = request.POST['title']
    desc = request.POST['desc']
    net = request.POST['network']
    release_date = request.POST['release_date']
    
    shows = Shows.objects.all()
    errors = Shows.objects.basic_valid(request.POST,shows)
    
    if len(errors) > 0:
        for key, error_msg in errors.items():
            messages.error(request, error_msg)
        return redirect(f'/shows/{show_id}/edit')
    
    show.title = title
    show.desc = desc
    show.network = Networks.objects.get(id=int(net))
    show.release_date = release_date
    try:
        show.save()
    except IntegrityError:
        messages.error(request,"This show alrready exist")
        return redirect(f'/shows/{show_id}/edit')

    messages.info(request, f'Show {show.title} has been edited')
    return redirect('/shows')

def delete(request,show_id):
    
    showdel = Shows.objects.get(id=int(show_id))
    showdel.delete()
    messages.warning(request, f'Show {showdel.title} has been deleted')
    return redirect('/shows')



