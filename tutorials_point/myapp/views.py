from myapp.models import Dreamreal
from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def hello(req):
    today = datetime.datetime.now()
    forecast = "There's a 45% chance of the following today: 1. SWAMP ASS 2. RAINING CATS AND DOGS 3. MORE SWAMP ASS"
    return render(req, "hello.html", {"today": today, "forecast": forecast})

def view_article(req, aid):
    article_id = None
    try:
        article_id = int(aid)
    except ValueError:
        article_id = -1
    text = "article no: %d" % (article_id)
    return HttpResponse(text)

def crudops(req):
    dreamreal = Dreamreal(
        website = "www.polo.com",
        mail = "sorex@polo.com",
        name = "sorex",
        phonenumber = "0987654321"
    )
    dreamreal.save()
    objects = Dreamreal.objects.all()
    res ='Printing all Dreamreal entries in the DB : <br>'

    for elt in objects:
        res += elt.name+"<br>"

    #Read a specific entry:
    sorex = Dreamreal.objects.get(name = "sorex")
    res += 'Printing One entry <br>'
    res += sorex.name

    #Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()

    #Update
    dreamreal = Dreamreal(
        website = "www.polo.com", mail = "sorex@polo.com", 
        name = "sorex", phonenumber = "002376970"
    )

    dreamreal.save()
    res += 'Updating entry<br>'

    dreamreal = Dreamreal.objects.get(name = 'sorex')
    dreamreal.name = 'thierry'
    dreamreal.save()

    return HttpResponse(res)