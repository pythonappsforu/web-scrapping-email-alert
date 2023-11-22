import requests
import selectorlib
from send_email import send_email
import time


URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
                      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
                      Mobile Safari/537.36'}
def scrape(url):
    response = requests.get(url,headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value

def store(value):
    with open("data.txt",'a') as file:
        file.write(value+'\n')
def read_file():
    with open("data.txt",'r') as file:
        return file.read()

if __name__ == "__main__":
    while True:
        source = scrape(URL)
        value = extract(source)
        print(value)
        if value != "No upcoming tours":
            text_values = read_file()
            if value not in text_values:
                store(value)
                message = f"Subject :New event found \n{value}"
                send_email(message)
                print("check mail")
        time.sleep(3)