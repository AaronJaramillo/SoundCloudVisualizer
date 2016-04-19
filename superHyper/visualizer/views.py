from django.shortcuts import render

from .forms import urlForm
from .models import URL 
from .SCVis import fetch 


# Create your views here.
def index(request):
    # return render(request, 'visualizer/home.html')
    form = urlForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('link'))
        fetch(form.cleaned_data.get('link'))
        
    context = {
        "form": form,
    }
    return render(request, "visualizer/home.html", context)