import requests
import selectorlib
from _datetime import datetime
import sqlite3


URL = "http://programmer100.pythonanywhere.com/"
HEADERS={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
                      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
                      Mobile Safari/537.36'}
def scrape(url):
    response = requests.get(url,headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('temp_extract.yaml')
    value = extractor.extract(source)['temperatures']
    return value
# using file as storage medium
def store(date,value):
    with open("temp_data.txt",'a') as file:
        file.write(f"{date},{value}")

# using db table temp_data
connection = sqlite3.Connection("data.db")

def db_store(date,value):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temp_data VALUES(?,?)",(date,value))
    connection.commit()

if __name__ == "__main__":
    source = scrape(URL)
    value = extract(source)
    date =  datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    #store(date,value+'\n')
    db_store(date,value)
    print(date,value)

