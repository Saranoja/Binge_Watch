import psycopg2


class Connection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="postgres",
                                               host="127.0.0.1",
                                               port="5432",
                                               database="BingeWatch")

            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
