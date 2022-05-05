from django.shortcuts import render
from . models import Course, Topnotch

# Create your views here.
def topnotch(request):
    english = Topnotch.objects.order_by('-create')
    context ={'english':english}
    return render(request , 'index.html' , context)


def vocabulary(request):
    vocab = Topnotch.objects.order_by('-create')
    context ={'vocab':vocab}
    return render(request , 'vocabulary.html', context)


def grammer(request):
    grammers = Topnotch.objects.order_by('-create')
    context ={ 'grammers' : grammers }
    return render(request , 'grammer.html' , context) 


def blog(request):
    # english = Topnotch.objects.order_by('-create')
    # context ={'english':english}
    return render(request , 'blog.html')

def speaking(request):
    speak = Topnotch.objects.order_by('-create')
    context ={'speak':speak}
    return render(request , 'speaking.html' , context)


# def shop(request):
#     return render(request , 'shop.html')


def sentences(request):
    sentence = Topnotch.objects.order_by('-create')
    context ={'sentence':sentence}
    return render(request , 'sentences.html' , context)

def home(request):
    # english = Topnotch.objects.order_by('-create')
    # context ={'english':english}
    return render(request , 'home.html' )


def shop(request):
    courses = Course.objects.order_by('-create')
    conext = {'courses' : courses}
    return render(request , 'shop.html' , conext )                
