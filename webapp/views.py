from django.shortcuts import render,HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('<h1>Hello Python Django framework</h1>')

# def about(request):
#     return HttpResponse("<h1>About Page<h1/>")

# def login(request):
#     return HttpResponse("<h1>Login page</h1>")


def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

def login(request):
    return render(request,'pages/login.html')