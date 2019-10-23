# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
import json
from mynewsite.common.CommORCL import CommORCL
import time


def coverage(request):
    context = {}  # 封装返回参数
    return render(request, 'coverage.html', context)


def coverageSearch(request):
    season = request.POST.get('season')
    flag = request.POST.get('progtype')
    orcl = CommORCL()
    getDateSQL = "select distinct update_date from MYSITE_PMOS_COVERATE_AUTOTEST order by update_date desc"
    updateList = orcl.query_List(getDateSQL)
    UPDATE_DATE = updateList[0]['UPDATE_DATE']
    timeArray = time.strptime(UPDATE_DATE, "%Y-%m-%d")
    updateMD = time.strftime("%m%d", timeArray)
    version = getVersionFromJDs(season);
    sel = 'select T.TEAM,T.UPDATE_DATE'
    From = " from "
    where = " where 1=1"
    orderby = " order by length(t.team),t.team"
    flags = ['T', 'M', 'N']
    i = 0
    for versions in version:
        sel = sel + ",NVL("+flags[i]+".COVEREDPROG,'-') as COVEREDPROG"+str(i)\
            + ",NVL("+flags[i] + ".ALLPROG,'-') as ALLPROG"+str(i)\
            + ",NVL(" + flags[i] + ".COVERATEPROG,'-') as COVERATEPROG" + str(i)\
            + ",NVL(" + flags[i] + ".COVERDBRANCH,'-') as COVERDBRANCH" + str(i)\
            + ",NVL(" + flags[i] + ".ALLBRANCH,'-') as ALLBRANCH" +str(i)\
            + ",NVL(" + flags[i] + ".COVERATEBRANCH,'-') as COVERATEBRANCH" + str(i)
        From = From + "MYSITE_PMOS_COVERATE_AUTOTEST "+flags[i]+","
        where = where + " and " +flags[i]+".UPDATE_DATE='"+UPDATE_DATE\
            + "' and "+flags[i]+".dept='北京开发四部'"\
            + " and "+flags[i]+".version='"+versions\
            + "' and "+flags[i]+".flag="+flag+""
        if i > 0:
            where = where + " and "+flags[i]+".TEAM = T.TEAM"
        i += 1
    From = From[0:len(From)-1]

    selsql = sel+From+where+orderby
    print(selsql)
    result=orcl.query_List(selsql)
    for cell in result:
        for j in range(0,i):
            COVERATEPROG = cell['COVERATEPROG'+str(j)]

            if COVERATEPROG[0]=='.':
                cell['COVERATEPROG'+str(j)] = '0'+COVERATEPROG
            elif COVERATEPROG=='%':
                cell['COVERATEPROG' + str(j)] = ''

            COVERATEBRANCH = cell['COVERATEBRANCH'+str(j)]

            if COVERATEBRANCH[0] == '.':
                cell['COVERATEBRANCH' + str(j)] = '0' + COVERATEBRANCH
            elif COVERATEBRANCH == '%':
                cell['COVERATEBRANCH' + str(j)] = ''

    readd = {'date':updateMD}
    result.append(readd);
    orcl.disconnect()
    print(result.__len__())
    data = {"total": result.__len__(), "rows": result}
    return HttpResponse(json.dumps(result, sort_keys=True), content_type="application/json")

def getVersionFromJDs(season):
    years = '20' + season[0:2]
    jd = season[3:4]
    version = []
    if jd == '1':
        version.append(years + '01')
        version.append(years + '02')
        version.append(years + '03')
    elif jd == '2':
        version.append(years + '04')
        version.append(years + '05')
        version.append(years + '06')
    elif jd == '3':
        version.append(years + '07')
        version.append(years + '08')
        version.append(years + '09')
    elif jd == '4':
        version.append(years + '10')
        version.append(years + '11')
        version.append(years + '12')

    return version