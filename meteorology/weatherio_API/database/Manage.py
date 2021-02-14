import mysql.connector


"""class Connection:

    def __init__(self):

        self.connector = None

    def generate_connection(self):

        connector = mysql.connector.connect(
            host="localhost",
            user="root_arturo",
            password="LikeAStone",
            database="MeteorologyPredictions"
        )

        return connector.cursor()

"""
connector = mysql.connector.connect(
    host="localhost",
    user="root_arturo",
    password="LikeAStone",
    database="MeteorologyPredictions"
)

# print(Connection().connector)()
cursor = connector.cursor()
cursor.execute("SHOW TABLES")
result = cursor.fetchall()

print(result)
for x in result:
    print(x)
