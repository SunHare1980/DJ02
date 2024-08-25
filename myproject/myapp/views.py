from django.shortcuts import render
from django.http import HttpResponse
def str1(request):
    return render(request, 'myapp/str1.html')
def str2(request):
    return render(request, 'myapp/str2.html')
def str3(request):
    return render(request, 'myapp/str3.html')
def str4(request):
    return render(request, 'myapp/str4.html')