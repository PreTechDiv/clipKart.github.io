from tkinter import Variable
from django.http import HttpResponse
from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request, "Form.html")

def about(request):
    return render(request, "About.html")

def search(request):
    
    search_value=request.POST.get("submit")
    search_value=search_value + ".jpg"
    context = {
        "search_value" : search_value
    }
    return render(request, "search.html" , context)