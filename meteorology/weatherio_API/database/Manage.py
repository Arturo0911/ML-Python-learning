import mysql.connector




class Connection:

    def __init__(self):
        
        self.connector = None


    def generate_connection(self):

        self.connector = mysql.connector.connect(
            host= "localhost",
            user= "root_arturo",
            password= "LikeAStone",
            database= "Meteorology"
        )