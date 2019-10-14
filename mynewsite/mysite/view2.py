# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse, Http404
import random, json
from mysite.models import Product
import pymysql   # 数据库驱动
from django.views.decorators import csrf
from datetime import date, datetime

# 数据库连接
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                             password='123qwe', db='webmott2', charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
# 创建数据库连接“执行”对象
cur = connection.cursor()


def delete2(request):
    id = request.POST.get('id')
    print("~~~~~~~~~~~~~~~~~~~~~~"+id+"=============")

    sql = "delete from auth_user where id='"+id+"'";
    # 执行sql语句

    try:
        # 执行sql语句
        cur.execute(sql)
        print("success")
        # 提交到数据库执行
        connection.commit()
    except:
        print("error")
        # 如果发生错误则回滚
        connection.rollback()

        # article = Article.objects.get(id=article_id)
    # article.delete()
    return_dict = {"ret": True, "errMsg": "", "rows": [], "total": 0}
    return HttpResponse(json.dumps(return_dict))