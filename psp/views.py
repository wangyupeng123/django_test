from django.shortcuts import render, redirect
from psp.models import BookInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext


# Create your views here.


def index(request):
    # return HttpResponse('老铁没毛病')
    # temp = loader.get_template('psp/index.html')
    # print('*'*50)
    # print(temp)
    # context = RequestContext(request,{'user': "wangyupeng"})
    # # context.push(locals())
    # print(context)
    # res_html = temp.render(context=locals())
    # print(res_html)
    # return HttpResponse(res_html)
    book = BookInfo.objects.all()
    return render(request, 'psp/index.html', {'books': book})


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
远程残酷
