import psycopg2


class DatabaseManager:
    conn = None
    host_ip = "localhost"
    database_name = "test01"
    user_id = "postgres"
    password = "win31big"

    @classmethod
    def build_conn(cls, host_ip=host_ip, database=database_name, user_id=user_id, password=password):
        if host_ip is None and database is None and user_id is None and password is None:
            try:
                cls.build_default_conn()
                print("Success to build connection to database")
            except Exception as e:
                print(e)
        else:
            try:
                cls.conn = psycopg2.connect(
                    host=host_ip,
                    database=database,
                    user=user_id,
                    password=password
                )
            except Exception as ex:
                print(ex)

    @classmethod
    def build_default_conn(cls):
        try:
            cls.conn = psycopg2.connect(
                host="localhost",
                database="test01",
                user="postgres",
                password="win31big"
            )
        except Exception as ex:
            print("Fail to build connection to default")
            print(ex)

    @classmethod
    def create_twse_single_stock_table(cls, table_name):
        if cls.conn is None:
            print("no database conn")
            return
        else:
            try:
                c = cls.conn.cursor()
                s = "CREATE TABLE " + str(
                    table_name) + " (pk serial PRIMARY KEY, id varchar(7), date date, volume integer, " \
                                  "amount bigint, start_price numeric(4,2), end_price numeric(4,2), " \
                                  "high numeric(4,2), low numeric(4,2), diff numeric(4,2), " \
                                  "trade_count smallint, yield numeric(3,2), yield_year varchar(4), " \
                                  "PER numeric(4,2), PBR numeric(4,2), value_year varchar(6)); "
                c.execute(s)
                cls.conn.commit()
                cls.conn.close()
            except Exception as err:
                print(err)

    @classmethod
    def create_twse_overview_table(cls):
        if cls.conn is None:
            print("no database conn")
            return
        else:
            try:
                c = cls.conn.cursor()
                s = "CREATE TABLE " + str(
                    table_name) + " (pk serial PRIMARY KEY, id varchar(7), date date, volume integer, " \
                                  "amount bigint, start_price numeric(4,2), end_price numeric(4,2), " \
                                  "high numeric(4,2), low numeric(4,2), diff numeric(4,2), " \
                                  "trade_count smallint, yield numeric(3,2), yield_year varchar(4), " \
                                  "PER numeric(4,2), PBR numeric(4,2), value_year varchar(6)); "
                c.execute(s)
                cls.conn.commit()
                cls.conn.close()
            except Exception as err:
                print(err)


    @staticmethod
    def update_twse_data_by_month(data: str):
        update_month = data[0: 5] + "01"
        stock_id = ""
