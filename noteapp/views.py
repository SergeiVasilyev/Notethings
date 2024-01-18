import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
import pytz
from datetime import datetime

from .models import Note, Category, Group

@login_required(login_url='/admin/login/')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/admin/login/')
def main(request):  
    all_notes = Note.objects.all().order_by('-updated_at')

    paginator = Paginator(all_notes, 30)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    context = {
        'all_notes': page,
    }
    return render(request, 'main.html', context)

@login_required(login_url='/admin/login/')
def note(request, idx):
    note = Note.objects.get(id=idx)
    context = {
        'note': note
    }
    return render(request, 'note.html', context)


@login_required(login_url='/admin/login/')
def create_note(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('tyni_text')

        now = datetime.now()
        datenow = pytz.utc.localize(now)

        group = 'main'
        group, folder_created = Group.objects.get_or_create(name=group)

        note = Note.create_note(text=text, name=name, creator=request.user, updated_at=datenow, group=group)
        return redirect('edit_note', note.id)
    
    return render(request, 'create_note.html')


@login_required(login_url='/admin/login/')
def edit_note(request, idx):
    note = Note.objects.get(id=idx)
    if request.method == 'POST':
        note.name = request.POST.get('name')
        note.text = request.POST.get('tyni_text')
        note.save()
        return redirect('edit_note', idx)
    
    context = {
        'note': note
    }
    return render(request, 'edit_note.html', context)


def logout_view(request):
    logout(request)
    return redirect('main')





@login_required(login_url='/admin/login/')
def new_note(request):
    cat_list = ['one3']
    cats = [Category.objects.get_or_create(name=cat)[0] for cat in cat_list]

    group = 'main'
    group, folder_created = Group.objects.get_or_create(name=group)

    now = datetime.now()
    datenow = pytz.utc.localize(now)

    name = 'The Second List of Top The Best Films'
    text = """"Nomadland" - Chloé Zhao
        "The Trial of the Chicago 7" - Aaron Sorkin
        "Promising Young Woman" - Emerald Fennell
        "Soul" - Pete Docter and Kemp Powers
        "Mank" - David Fincher
        "Minari" - Lee Isaac Chung
        "Judas and the Black Messiah" - Shaka King
        "Sound of Metal" - Darius Marder
        "Dune" - Denis Villeneuve
        "A Quiet Place Part II" - John Krasinski"""
    note = Note.create_note(text=text, name=name, creator=request.user, category=cats, group=group, updated_at=datenow)

    return redirect('main')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             return render(request, 'main.html')
#         else:
#             return render(request, 'login.html')
        
#     return render(request, 'login.html')