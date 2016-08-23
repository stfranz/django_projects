from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def hello(req):
    today = datetime.datetime.now()
    return render(req, "hello.html", {"today": today})

def view_article(req, aid):
    article_id = None
    try:
        article_id = int(aid)
    except ValueError:
        article_id = -1
    text = "article no: %d" % (article_id)
    return HttpResponse(text)