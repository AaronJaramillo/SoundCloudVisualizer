from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<html><body bgcolor=\"#FFFFFF\"><h2><font face=\"verdana\" color=\"black\"><center>Sound Cloud Visualizer</center></font></h2><form><center>Soundcloud URL:<br><input type=\"text\" name=\"Soundcloud URL: \"><br></center></form></body></html>")
