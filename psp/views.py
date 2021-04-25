from django.shortcuts import render, redirect
from psp.models import BookInfo,HeroInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader, RequestContext


# Create your views here.


def index(request):
    return render(request, 'psp/index.html')


def show_books(request):
    """显示图书信息"""
    books = BookInfo.objects.all()
    return render(request, 'psp/show_book.html', {'books': books})


def show_book_detial(request, btitle):
    detial = BookInfo.objects.get(btitle=btitle)
    heros = detial.heroinfo_set.all()
    return render(request, 'psp/show_book_detial.html', {'heros':heros, 'detial':detial})


def creat(request):
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpup_date = date(2000, 3, 27)
    # b.bread = 20,
    # b.bcomment = 3,
    # b.isDelete = False
    b.save()
    # return HttpResponseRedirect(redirect_to='/index')
    return redirect('/index')


def delete(request, id):
    b = BookInfo.objects.get(id=id)
    b.delete()
    return HttpResponseRedirect('/index')


def login(request):
    return render(request, 'psp/login.html')


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    datas = HeroInfo.objects.all()
    for data in datas:
        # print(data.hname, data.hcomment)
        if username == data.hname and password == data.hcomment:
            return render(request, 'psp/login_check.html',{'username':username,'password':password})
    return redirect('/login')


def ajax_test(request):
    return render(request, 'psp/ajax.html')


def ajax_handel(request):
    return JsonResponse({'user': 'wangyupeng'})
