import sqlite3
import re


class PassengerModel:

    def __init__(self, data):

        self.passenger_data = data


    def register_passenger(self):

        if self._registered_passenger():
            return False
        else:
            connection = sqlite3.connect('./data/ride_share.db')
            cursor = connection.cursor()

            query = "INSERT INTO passengers (passenger_name, phone_number, whatsapp_link) VALUES (?, ?, ?);"

            whatsapp_link = self._get_whatsapp_link(self.passenger_data['phone_number'])

            cursor.execute(query, (self.passenger_data['passenger_name'], 
                                self.passenger_data['phone_number'],
                                whatsapp_link))

            connection.commit()
            connection.close()

            return True


    def _registered_passenger(self):

        connection = sqlite3.connect('./data/ride_share.db')
        cursor = connection.cursor()

        query = f'SELECT COUNT(*) FROM passengers WHERE phone_number = ?'

        cursor.execute(query, (self.passenger_data['phone_number'],))

        result = cursor.fetchone()

        connection.close()

        if result[0] == 0:
            return False
        else:
            return True
        

    def _get_whatsapp_link(self, phone_number):
        number = re.findall(r'\d+', phone_number)
        formated_number = ''.join(number)
        whatsapp_link = f"https://wa.me/{formated_number}"
        return whatsapp_link


    