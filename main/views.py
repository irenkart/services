from django.shortcuts import render, render_to_response
import requests
from bs4 import BeautifulSoup
from .models import *


# Create your views here.
def home(request):
    return render_to_response('base.html')
