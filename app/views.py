from django.http import HttpResponse
from django.shortcuts import render
from .utils import jb_windows

# Create your views here.

def test(request):
    return HttpResponse(jb_windows.get_basic_indicators())