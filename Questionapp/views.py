from django.shortcuts import render
from .models import q_a
from django.http import *


def index(request):
    Questionapp = q_a.objects.all()
    return render(request, 'base.html', {'Questionapp': Questionapp})
   # return HttpResponse('index.html')
  #  return HttpResponseRedirect('/Questionapp/')
