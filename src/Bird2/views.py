from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# function based view
def home(request):
    return HttpResponse('hello home ..')
    # return render(request, 'home.html', {})  #response