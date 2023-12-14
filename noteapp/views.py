from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate

from .models import Note, Category, Folder
from .services import create_note



@login_required(login_url='/admin/login/')
def main(request):  
    # cat_list = ['one', 'two3', 'three']
    # cats = [Category.objects.get_or_create(name=cat)[0] for cat in cat_list]

    # folder = 'main2'
    # folder, folder_created = Folder.objects.get_or_create(name=folder)

    # name = 'Some name2'
    # text = "Some interesting text 2"
    # note = create_note(text=text, name=name, creator=request.user, category=cats, folder=folder)

    all_notes = Note.objects.all()

    context = {
        # 'note': note,
        'all_notes': all_notes
    }
    return render(request, 'main.html', context)

@login_required(login_url='/admin/login/')
def new_note(request):
    cat_list = ['one3']
    cats = [Category.objects.get_or_create(name=cat)[0] for cat in cat_list]

    folder = 'main'
    folder, folder_created = Folder.objects.get_or_create(name=folder)

    name = 'The Second Best music list'
    text = """Olivia Rodrigo - "drivers license"
            Lil Nas X - "Montero (Call Me By Your Name)"
            The Weeknd - "Save Your Tears"
            Dua Lipa - "Levitating"
            Ed Sheeran - "Bad Habits"
            Adele - "Easy On Me"
            Justin Bieber - "Peaches" (ft. Daniel Caesar & Giveon)
            Doja Cat - "Kiss Me More" (ft. SZA)
            Bruno Mars, Anderson .Paak - "Leave The Door Open" (as Silk Sonic)
            Billie Eilish - "Therefore I Am"""
    note = create_note(text=text, name=name, creator=request.user, category=cats, folder=folder)

    context = {
        'note': note
    }
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