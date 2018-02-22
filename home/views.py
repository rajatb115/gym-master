from django.shortcuts import render_to_response, get_object_or_404
from .models import About

# Create your views here.
def index(request):
    return render_to_response('home/index.html',{
        'items': About.objects.all()
    })