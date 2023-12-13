from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate

from .models import Note, Category, Folder
from .services import create_note



@login_required(login_url='/admin/login/')
def main(request):
    print(request.user)
    
    cat_list = ['one', 'two3', 'three']
    cats = [Category.objects.get_or_create(name=cat)[0] for cat in cat_list]

    folder = 'main2'
    folder, folder_created = Folder.objects.get_or_create(name=folder)
    print('folder', folder)

    name = 'Some name2'
    text = "Some interesting text 2"
    note = create_note(text=text, name=name, creator=request.user, category=cats, folder=folder)

    context = {
        'note': note
    }
    return render(request, 'main.html', context)


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