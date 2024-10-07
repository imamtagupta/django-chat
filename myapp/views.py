from django.shortcuts import render

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

