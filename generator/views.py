from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    #return HttpResponse("Hello there!!!")
    return render(request , 'generator/home.html' , {'password': 'losowehasło'})

def password(request):
    characters = list('abcdefghijklmnoprstuvwxyz')
    charactersUpper = list(' ABCDEFGHIJKLMONPRSTUWXYZ')
    charactersSpecial = list('!@#$%^&*()')
    charactersNumbers = list('123456789')
    characters.extend(charactersUpper)
    characters.extend(charactersSpecial)
    characters.extend(charactersNumbers)
    lenght = int(request.GET.get('lenght', 12))
    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})