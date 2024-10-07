from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse


# Create your views here.


def index(request):
    print("Rendering base page")
    return render(request, 'myapp/index.html')


def room(request, room_name):
    return render(request, 'myapp/chat.html', {
        'room_name': room_name
    })

def base(request):
    print("base page is getting rendered")
    return render(request, 'myapp/base.html')

def get_users(request):
    users = User.objects.all().values('id', 'username', 'email')
    users_list = list(users)  # Convert QuerySet to list
    return JsonResponse(users_list, safe=False)


def save_user(request, uname):
    user = User(username=uname)
    user.save()

    