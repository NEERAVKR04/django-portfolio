from django.shortcuts import render

# Create your views here.
def hello(request):
    return render('','hello_world.html',{})
