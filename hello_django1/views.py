from django.http import HttpResponse
from django.shortcuts import render


# def about(request): # пользователь делает request-запрос
#     return HttpResponse('This is my first page') #его перенаправляют на страаницу с написью This is my first page

# def about(request): # пользователь делает request-запрос
#     return render(request,'about.html',{'gretting':'hello'})# мы хотим,чтобы не нашу страницу вывоилось все,что содержится в файле about.html


def about(request):
    a=5+6
    return render(request, 'about.html', {'gretting': a})

def home(request):
    return HttpResponse('This is my home')