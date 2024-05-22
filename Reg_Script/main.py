import wikipedia as wiki
import requests as rq
from bs4 import BeautifulSoup
import regex

search = input("Page Title: ")
results = wiki.search(search, results=5)

count = 1
for result in results:
    print(f"{count} -- {result}")
    count += 1

pick = int(input("Which one would you like to summarize? "))

url = "https://en.wikipedia.org/wiki/"
match pick:
    case 1:
        url += results[0]
    case 2:
        url += results[1]
    case 3:
        url += results[2]
    case 4:
        url += results[3]
    case 5:
        url += results[4]
    case _:
        print("Invalid input")

try:
    rq_response:rq.Response = rq.get(url)
except rq.HTTPError:
    print("Error: Invalid URL")

soup = BeautifulSoup(rq_response.text, 'lxml')
list_of_p = soup.find_all('p')

# Clean out [0]s
for i in range(len(list_of_p)):
    list_of_p[i] = regex.sub(r'\[\d\]', '', list_of_p[i].get_text())
    print(list_of_p[i])
