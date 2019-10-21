# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse, Http404
import random, json
from mysite.models import Product
from mynewsite.common.CommORCL import CommORCL
import pymysql  # 数据库驱动
from django.views.decorators import csrf
from datetime import date, datetime




def index(request):
    context = {}  # 封装返回参数
    sql = "select * from auth_user"
    # 执行sql语句
    # 获取所有记录列表
    commORCL = CommORCL()
    results = commORCL.query_List(sql)
    commORCL.disconnect()
    context['items'] = results  # 存入集合
    quotes = ['今日事，今日毕',
              '要怎么收获，先那么栽',
              '知识就是力量',
              '一个人的个性就是他的命运']
    quote = random.choice(quotes)
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', locals())


def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())


def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的产品编号')
    return render(request, 'disp.html', locals())


def ajax_add(request):
    num1 = request.GET.get("i1")
    num2 = request.GET.get("i2")
    ret = int(num1) + int(num2)
    return HttpResponse(ret)


def findresult(request):
    if request.method == 'GET':
        pageSize = int(request.GET.get('rows'))
        pageNumber = int(request.GET.get('page'))
        print(pageSize)
        print(pageNumber)
        # searchText = request.GET.get('searchText')
        # sortName = request.GET.get('sortName')
        # sortOrder = request.GET.get('sortOrder')
    # print(num1)
    sql = "select id,username,password,email,to_char(date_joined,'YYYY-mm-dd HH24:MI:SS') BirthDate from auth_user where username ='admin' "
    # 执行sql语句
    commORCL = CommORCL()
    results = commORCL.query_List(sql)
    commORCL.disconnect()
    # 获取所有记录列表
    # reCount = cur.execute('insert into UserInfo(Name,Address) values(%s,%s)', ('alex', 'usa'))
    #results = [{'id': 1, 'username': 'admin', 'password': 'pbkdf2_sha256$150000$CR59ZqpHz2fO$9vPYn49tWiNwGOtbflHV7vE1K7TCbgLPS+Ok4rbJKvc=', 'email': '', 'BirthDate': '2019-10-11 08:October:47'}]
    # rows = []
    print(results)
    print("test666666----------------------------------")

    data = {"total": results.__len__(), "rows": results}
    return HttpResponse(json.dumps(data, sort_keys=True), content_type="application/json")

    # return HttpResponse(items)
    # return HttpResponse(json.dumps(items, sort_keys=True), content_type="application/json")
    # return JsonResponse(items)


def delete(request):
    id = request.POST.get('id')
    print(id + "=============")

    sql = "delete from auth_user where id='" + id + "'";
    # 执行sql语句

    try:
        # 执行sql语句
        # cur.execute(sql)
        print("success")
        # 提交到数据库执行
        # connection.commit()
    except:
        print("error")
        # 如果发生错误则回滚
        # connection.rollback()

        # article = Article.objects.get(id=article_id)
    # article.delete()
    return_dict = {"ret": True, "errMsg": "", "rows": [], "total": 0}
    return HttpResponse(json.dumps(return_dict))
