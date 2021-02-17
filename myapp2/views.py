from django.shortcuts import render

# Create your views here.
def regFun(request):
    return render(request,'register.html')
def homefn(request):
    return render(request,'home.html')
def dashfun(request):
    return render(request,'dashboard.html')