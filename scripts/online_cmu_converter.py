from bs4 import BeautifulSoup as BS
import requests
import shelve
from tqdm import tqdm

############# NEED TO RUN THIS SCRIPT FROM LOCAL MACHINE #######
### bs4 not on kuno

url = "http://www.speech.cs.cmu.edu/cgi-bin/cmudict"
query_pre = "?in="
cache = shelve.open("cache.data")
data = {}

def url_get(url):
    url = str(url)
    if url in cache:
        data = cache[url]
        return BS(data, 'html.parser')

    data = requests.get(url).text
    cache[url] = data
    return BS(data, 'html.parser')

def get_pronunciation(data):
    result = data.find_all("tt")[1]
    result = str(result)
    result = result.replace("<tt>", "")
    result = result.replace("</tt>", "")
    result = result[:-2]
    return result

if __name__ == "__main__":
    data = {}
    cmu = {}
    
    with open("words.txt", "r") as f:
        words = f.read()
        words = words.split("\n")

    for word in words:
        if word == "":
            words.remove(word)

    for word in tqdm(words):
        page = url_get(url + query_pre + word)        
        cmu[word] = get_pronunciation(page)

    with open("out.txt", "w") as f:
        for word in words:
            f.write(word + "\t" + cmu[word])
            f.write("\n")
