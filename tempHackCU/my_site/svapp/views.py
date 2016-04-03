from django.shortcuts import render
from django.http import HttpResponse
import SCVis

# Create your views here.

def index(request):
	return render(request, 'svapp/home.html');

def fireURL(request):
	return render(request, 'svapp/simpleform.asp');

def extract(request):

	SCVis.main(request);
