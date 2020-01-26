from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Imagemodels
from .form import Imagemodelform
# Create your views here.

def home(request):
    if request.method =="POST":
        nam =request.POST.get('name')
        imag=request.POST.get('image')
        print(imag)
        Imagemodels.objects.create(name=nam,image=imag)

    return render(request,'home.html')

class image(CreateView):
    model = Imagemodels
    form_class = Imagemodelform
    template_name = 'home.html'
    success_url = reverse_lazy('image')