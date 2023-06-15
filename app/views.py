from django.shortcuts import render

# Create your views here.
def mdb5(request):
    return render(request,'mdb5.html')
def mdb5child(request):
    return render(request,'mdb5child.html')