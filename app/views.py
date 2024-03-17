from django.shortcuts import render
from django.http import HttpResponse

from .models import Carousel
# Create your views here.


def home(request):
    obj = Carousel.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'index.html', context)


