

import mysql.connector

class Connection:

    def __init__(self):

        self.cursor = None


    def get_connection(self):
        

        self.cursor = mysql.connector.connect(
                
                host = "localhost",
                user = "root_arturo",
                password = "LikeAStone",
                database = "MeteorologyPredictions"
                )

        return self.cursor



connection = Connection()


cursor = connection.get_connection().cursor()
cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)








