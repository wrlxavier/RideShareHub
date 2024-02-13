import sqlite3
import pandas as pd


class PassengersModel:

    def __init__(self):
        self.passengers = []
        

    def get_all_passengers(self):

        connection = sqlite3.connect('./data/ride_share.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM passengers ORDER BY passenger_name;'
        cursor.execute(query)
        result = cursor.fetchall()

        columns = [description[0] for description in cursor.description]
        df = pd.DataFrame(result, columns=columns)

        connection.close()
        return df

    