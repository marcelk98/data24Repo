import pyodbc

class NwProducts:
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' +
                                               self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all_product_records(self):
        query_records = self._sql_query("SELECT * FROM Products")
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)

    def print_average_unit_price(self):
        avgprice = self._sql_query("SELECT avg(UnitPrice)"
                                   "From Products").fetchone()
        print("The average price is",avgprice)

nwp = NwProducts()
nwp.print_average_unit_price()

