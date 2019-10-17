import cx_Oracle


class CommORCL:

    def __init__(self, ip):
        self.connection = cx_Oracle.connect('BJ4USER/BJ4USER@' + ip + ':1521/orcl')
        self.cur = self.connection.cursor()

    def query_Dict(self, SQL):
        self.cur.execute(SQL)
        results = self.cur.fetchall()
        cols = [d[0] for d in self.cur.description]
        print(results)
        re = []
        for row in results:
            b = dict(zip(cols, row))
            re.append(b)

        print(re)
        return re

    def disconnect(self):
        self.cur.close()
        self.connection.close()
