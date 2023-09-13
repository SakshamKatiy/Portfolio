from django.shortcuts import render
from .models import message
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        a= message.objects.create(
            name=name,
            email=email,
            msg=msg
        )
       
    return render(request,'index.html')