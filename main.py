import requests
import selectorlib
from send_email import send_email
import time
import sqlite3


URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
                      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
                      Mobile Safari/537.36'}


class Events:
    def scrape(self,url):
        response = requests.get(url,headers=HEADERS)
        source = response.text
        return source

    def extract(self,source):
        extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
        value = extractor.extract(source)['tours']
        return value

class Database:
    def __init__(self):
        self.connection = sqlite3.Connection("data.db")
    # functions for reading and storing in file
    def store(self,value):
        with open("data.txt",'a') as file:
            file.write(value+'\n')
    def read_file(self):
        with open("data.txt",'r') as file:
            return file.read()

    # functions for reading and storing in SQLite DB


    def read_db(self,extracted_value):
        row = extracted_value.split(',')
        band,city,date = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?",
                       (band,city,date))
        return cursor.fetchall()


    def db_store(self,extracted_value):
        row = extracted_value.split(',')
        band, city, date = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)",
                       (band, city, date))
        self.connection.commit()

if __name__ == "__main__":
    event = Events()
    database = Database()
    while True:
        source = event.scrape(URL)
        extracted_value = event.extract(source)
        print(extracted_value)
        if extracted_value != "No upcoming tours":
            # text_values = read_file()
            db_values = database.read_db(extracted_value)
            if not db_values:
                database.db_store(extracted_value)
                message = f"Subject :New event found \n{extracted_value}"
                send_email(message)
                print("check mail")
        time.sleep(3)