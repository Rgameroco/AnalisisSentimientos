from django.http import HttpResponse
from django.template.loader import get_template

def index(request):
    t = get_template('index.html')
    c= {'foo':'bar'}
   # apiT()
    return HttpResponse(t.render(c,request))