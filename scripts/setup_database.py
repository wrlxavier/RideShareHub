import sqlite3
import json


def run_script():

    connection = sqlite3.connect(f'../data/ride_share.db')
    cursor = connection.cursor()

    try:
        with open('db_config.json', 'r') as db_config_file:
            db_config = json.load(db_config_file)


        for file_name in db_config['ordered_queries']:
            file_path = f'./sql/{file_name}.sql'
            try:
                with open(file_path, 'r') as query_file:
                    query = query_file.read()
                    cursor.execute(query)
                print(f'The "{file_name}.sql" query was executed successfully.')

            except:
                print(f'Unable to open or execute file "{file_name}.json"')

    except:
        print('Unable to open file "db_config.json"')

    connection.commit()
    connection.close()


if __name__=='__main__':
    run_script()
