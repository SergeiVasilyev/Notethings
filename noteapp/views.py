import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
import pytz
from datetime import datetime

from .models import Note, Category, Group


def home(request):
    return render(request, 'home.html')


@login_required(login_url='/admin/login/')
def main(request):  
    all_notes = Note.objects.all()

    context = {
        'all_notes': all_notes,
    }
    return render(request, 'main.html', context)


def card(request, idx):
    note = Note.objects.get(id=idx)
    context = {
        'note': note
    }
    return render(request, 'card.html', context)



# Cards for Ajax
@login_required(login_url='/admin/login/')
def get_cards(request):
    all_notes = list(Note.objects.values('id', 'name', 'text', 'updated_at'))

    return JsonResponse(all_notes, safe=False)


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

def edit_card(request, idx):
    note = Note.objects.get(id=idx)
    if request.method == 'POST':
        note.name = request.POST.get('name')
        note.text = request.POST.get('editor_content')
        note.save()
        return redirect('main')
    context = {
        'note': note
    }
    return render(request, 'edit_card.html', context)


def logout_view(request):
    logout(request)
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