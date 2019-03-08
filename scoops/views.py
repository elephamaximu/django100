from django.shortcuts import render, HttpResponse

# Create your views here.

def func1(request):
    return HttpResponse("응답1")

def func2(request, year):
    return HttpResponse("응답2.....param:{}".format(year))

def func3(request, year, month):
    return HttpResponse("응답3.....param:{}..{}".format(year, month))

def func4(request, aa):
    return HttpResponse("응답4...param:{}".format(aa))

def func5(request, aa, bb):
    return HttpResponse("응답5.....param:{}..{}".format(aa, bb))

def func6(request, year, month, myname):
    return HttpResponse("응답6.....param:{}..{}..{}".format(year, month, myname))


def func7(request, num):
    print("views.py.......", num, type(num))
    return HttpResponse("응답7.....param:{}".format(num))