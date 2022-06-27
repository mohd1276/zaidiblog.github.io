from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.



def index(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request, 'index.html', {'myposts': myposts})
    
def about(request):
    return render(request, 'about.html')

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blogpost.html',
                  {'post':post})
  