import requests
import selectorlib
from _datetime import datetime


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

def store(date,value):
    with open("temp_data.txt",'a') as file:
        file.write(f"{date},{value}")



if __name__ == "__main__":
    source = scrape(URL)
    value = extract(source)
    date =  datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    store(date,value+'\n')

