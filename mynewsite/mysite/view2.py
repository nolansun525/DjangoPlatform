# _*_ coding: utf-8 _*_
import cx_Oracle
from django.http import HttpResponse, Http404
import random, json


# 数据库连接
connection = cx_Oracle.connect('BJ4USER/BJ4USER@localhost:1521/orcl')

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