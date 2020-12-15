from django.shortcuts import render
from .models import Gallerie


def all_galleries(request):
    galleries = Gallerie.objects.order_by('-date')
    return render(request, 'gallerie/all_galleries.html', {'galleries': galleries})
