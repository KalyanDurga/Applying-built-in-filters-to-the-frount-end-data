from django.shortcuts import render

# Create your views here.

def display_filters(request):
    d={'A':'hII HoW aRE YoU','c':1,'d':16}



    return render(request,'display_filters.html',d)

