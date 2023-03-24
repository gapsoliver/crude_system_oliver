from django.shortcuts import render

def displyindex(request):
    return render(request, "index.html")