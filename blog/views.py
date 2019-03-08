from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.http import Http404, JsonResponse
from .models import Post
from django.template import loader
import os
from django.conf import settings
import pandas as pd
from io import StringIO
from urllib.parse import quote


def get_redirect1(request):
    return redirect("/blog/postlist/")
    #return redirect("postlist/")

def get_redirect2(request):
    return redirect("http://www.google.com")    


def pandas_csv(request):
    df = pd.DataFrame([[10,20,30,40],
                       ["seoul","busan","daejun","inchun"],
                       ["서울", "부산","대전","인천"]
                       ])
    io = StringIO()
    df.to_csv(io)
    io.seek(0)

    #filename = quote("pandas_csv.csv")
    filename = "pandas_csv.csv"
    response = HttpResponse(io, content_type="text/csv")
    response["Content-Disposition"] = "attachment;filename={}".format(filename)
    return response





def excel_download(request):
    filename = "demo.xlsx"
    #실제경로 
    filepath =  os.path.join(settings.BASE_DIR, filename)
    print("settings.BASE_DIR:", settings.BASE_DIR)
    print("실제경로 :", filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type="application/vnd.ms-excel")
        response["Content-Disposition"] = "attachment;filename={}".format(filename)
    return response





def json_test(request):
    music = {"가수":"BTS", "sings":["FAKE LOVE", "DNA", "피땀눈물"] }
    return JsonResponse(music, json_dumps_params={"ensure_ascii":False})




# Create your views here.
def post_detail(request, post_id):
    #방법3
    #p = get_object_or_404(Post, pk=post_id)
    #return render(request, "blog/postdetail.html", { "post" : p })

    #방법2
   
    try:
        p = Post.objects.get(pk=post_id)
    except  Post.DoesNotExist:
        raise  Http404("Post가 존재하지 않습니다.")  
    return render(request, "blog/postdetail.html", { "post" : p })
    
    #방법1
    #return HttpResponse("상세보기:" + str(post_id))

def post_list(request):
    #방법3
    plist = Post.objects.all()
    return render(request, "blog/postlist.html", { "post_list" : plist })

    #방법2
    # plist = Post.objects.all()
    # template = loader.get_template("blog/postlist.html")
    # context = { "post_list" : plist }
    # return HttpResponse(template.render(context, request))

    #방법1
    # plist = Post.objects.all()
    # str = ','.join([p.title for p in plist])
    # return HttpResponse(str)


def index(request):
    print("path:", request.path)
    print("요청방식:", request.method)
    return HttpResponse("Hello 장고프로젝트....응답합니다.")

def test1(request):
    return HttpResponse("test1메서드로 응답합니다.")

def test2(request):
    return HttpResponse("test2메서드로 응답합니다.")

def test3(request, year):
    print(year)
    return HttpResponse("test3메서드로 응답합니다.{}".format(year))

def test4(request, year):
    print(year)
    return HttpResponse("test4메서드로 응답합니다.{}".format(year))

def test5(request, year):
    print(year)
    return HttpResponse("test5메서드로 응답합니다.{}".format(year))  

def test6(request, year, month):
    print(year, month)
    return HttpResponse("test6메서드로 응답합니다.{}년도 {}월".format(year, month))    
