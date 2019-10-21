# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
import  json
from mynewsite.common.CommORCL import CommORCL


def coverage(request):
    context = {}  # 封装返回参数
    return render(request, 'coverage.html', context)


def coverageSearch(request):
    inputYear = request.GET.get('inputYear')
    # pageSize = request.GET.get('rows')
    # pageNumber = request.GET.get('page')
    # sortName = request.GET.get('sort')
    # sortOrder = request.GET.get('sortOrder')
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # print("inputYear:" + inputYear)

    # searchText = request.GET.get('searchText')
    # sortName = request.GET.get('sortName')
    # sortOrder = request.GET.get('sortOrder')
    # print(num1)
    strWhere = ""  # 查询条件
    strPage = ""  # 分页和排序
    if (inputYear != None and inputYear != ''):
        strWhere = " where username ='" + inputYear + "'"

    # if (sortName != None):
    #     strPage = " order by " + sortName + " " + sortOrder
    # startNumber = (int(pageSize) * int(pageNumber) - 1)  # 每页数量*页码 减1
    # print("startNumber:" + str(startNumber))
    # endNumber = int(pageNumber) * int(pageSize)
    # strPage += " limit " + str(startNumber) + "," + str(endNumber)


    commORCL = CommORCL('localhost')
    sql = "select * from MYSITE_PMOS_COVERATE_AUTOTEST  "
    # 执行sql语句
    results = commORCL.query_List(sql)
    print(results)
    commORCL.disconnect()


    data = {"total": results.__len__(), "rows": results}
    return HttpResponse(json.dumps(data, sort_keys=True), content_type="application/json")

