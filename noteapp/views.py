from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
import pytz
from datetime import datetime

from .models import Note, Category, Group



@login_required(login_url='/admin/login/')
def main(request):  
    all_notes = Note.objects.all()

    context = {
        'all_notes': all_notes
    }
    return render(request, 'main.html', context)

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