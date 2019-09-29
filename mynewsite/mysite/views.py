# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse, Http404
import random, json
from mysite.models import Product
import pymysql   # 数据库驱动
from django.views.decorators import csrf


# 数据库连接
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                             password='3E_DRHN@eeechina.cn', db='webmott2', charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
# 创建数据库连接“执行”对象
cur = connection.cursor()

def index(request):
    quotes = ['今日事，今日毕',
            '要怎么收获，先那么栽',
            '知识就是力量',
            '一个人的个性就是他的命运']
    quote = random.choice(quotes)
    return render(request, 'index.html', locals())


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
    num1 = request.GET.get("i1")
    num2 = request.GET.get("i2")
    print(num1)
    items = []
    testline = {}
    for i in range(10):
        testline['name'] = "nxy"
        testline['id'] = "123456"
        items.append(testline.copy())

    # return HttpResponse(items)
    return HttpResponse(json.dumps(items, sort_keys=True), content_type="application/json")
    # return JsonResponse(items)

