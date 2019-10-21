from mynewsite.common.CommORCL import CommORCL

sql = "select id,username,password,email,to_char(date_joined,'YYYY-mm-dd HH24:MI:SS') BirthDate from auth_user where username ='admin' "
commORCL = CommORCL('localhost')
re = commORCL.query_List(sql)
commORCL.disconnect()