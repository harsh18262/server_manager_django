from django.shortcuts import render

# Create your views here.
def testing(request):

    return render(request, "index1.html")
