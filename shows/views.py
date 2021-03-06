from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.db import IntegrityError
import bcrypt
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return redirect("/login")

def shows(request):
    if 'user' not in request.session:
        return redirect('/login')
        
    else:
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
    img = request.POST['img']
    shows = Shows.objects.all()
    errors = Shows.objects.basic_valid(request.POST,shows)
    
    if len(errors) > 0:
        for key, error_msg in errors.items():
            messages.error(request, error_msg)
        return redirect('/shows/new')
    try:
        new_show = Shows.objects.create (title = title, desc = desc , network = Networks.objects.get(id=int(net)), release_date = release_date, img=img)
    except IntegrityError:
        messages.error(request,"This show already exist")
        return redirect('/shows/new')
        
    messages.success(request, f'Show {title} has been Created')
    return redirect(f"/shows/{new_show.id}")

#@login_required
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
    img = request.POST['img']
    
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
    show.img = img
    try:
        show.save()
    except IntegrityError:
        messages.error(request,"This show already exist")
        return redirect(f'/shows/{show_id}/edit')

    messages.info(request, f'Show {show.title} has been edited')
    return redirect('/shows')

def delete(request,show_id):
    
    showdel = Shows.objects.get(id=int(show_id))
    showdel.delete()
    messages.warning(request, f'Show {showdel.title} has been deleted')
    return redirect('/shows')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')

    else:

        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        pass_conf = request.POST['pass_conf']
        

        if password != pass_conf:
            messages.error(request, 'Passwords dont coincide')
            return redirect('/signup')
        
        errors = Users.objects.user_valid(request.POST)
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        if len(errors) > 0:
            for key, error_msg in errors.items():
                messages.error(request, error_msg)
            return redirect('/signup')
        try:
            new_user = Users.objects.create(
            name=name,
            email=email,
            password=pw_hash)
        except IntegrityError:
            messages.error(request,"This Username/Email is already in use")
            return redirect('/signup')

        request.session['user'] = {'name':name}
        # xq estaban 'email':email,'password':password en session?
                                

        messages.success(request,f'Welcome {name} to TvShows')
        return redirect('/shows')

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    
    else:
        username = request.POST['name']
        password = request.POST['password']

        user = Users.objects.filter(name = username)
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
                request.session['user'] = {'name':username}
                
                messages.success(request,f'Welcome {username} to TvShows')
                return redirect('/shows')
            else:
                messages.error(request,"Invalid Username/Password")
                return redirect('/login')


def logout(request):
    del request.session['user']
    return redirect('/login')