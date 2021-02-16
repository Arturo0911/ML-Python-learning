

import mysql.connector



LIST_CLOUDS = ['Overcast_clouds','Broken_clouds','Few_clouds', 'Clear_Sky','Light_rain','Scattered_clouds']



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


    def insertion(self, path, year):
        pass

    
    def creation_tables(self, table_name):
        
        # tables name
        # time_start,time_end,cloud_description,relative_humidity,clouds,precip,temperature,icon,code
        # list_clouds = ['Overcast_clouds','Broken_clouds','Few_clouds', 'Clear_Sky','Light_rain','Scattered_clouds']
        cursor = self.get_connection().cursor()
        cursor.execute("CREATE TABLE {} (id int(11) PRIMARY KEY AUTO_INCREMENT, time_start varchar(30), time_end varchar(30), cloud_description varchar(50), relative_humidity decimal(13,4), clouds int, precip decimal(13,4), temperature decimal(13,4), icon varchar(10), code varchar(10))".format(table_name))







connection = Connection()

for x in LIST_CLOUDS:
    connection.creation_tables(str(x))








